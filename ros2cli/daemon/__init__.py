# Copyright 2017-2021 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import os
import time
import uuid

import rclpy
import rclpy.action

from ros2cli.helpers import before_invocation
from ros2cli.helpers import bind
from ros2cli.helpers import get_ros_domain_id
from ros2cli.helpers import pretty_print_call

from ros2cli.node.network_aware import NetworkAwareNode

from ros2cli.xmlrpc.local_server import LocalXMLRPCServer
from ros2cli.xmlrpc.local_server import SimpleXMLRPCRequestHandler


def get_port():
    base_port = 11511
    base_port += int(os.environ.get('ROS_DOMAIN_ID', 0))
    return base_port


def get_address():
    return '127.0.0.1', get_port()


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/ros2cli/',)


def get_xmlrpc_server_url(address=None):
    if not address:
        address = get_address()
    host, port = address
    path = RequestHandler.rpc_paths[0]
    return f'http://{host}:{port}{path}'


def make_xmlrpc_server() -> LocalXMLRPCServer:
    """Make local XMLRPC server listening over ros2cli daemon's default port."""
    address = get_address()

    return LocalXMLRPCServer(
        address, logRequests=False,
        requestHandler=RequestHandler,
        allow_none=True
    )


def serve(server: LocalXMLRPCServer, *, timeout: int = 2 * 60 * 60):
    """
    Serve the ros2cli daemon API using the given `server`.

    :param server: an XMLRPC server instance
    :param timeout: how long to wait before shutting
      down the server due to inactivity.
    """
    ros_domain_id = get_ros_domain_id()
    node_args = argparse.Namespace(
        node_name_suffix=f'_daemon_{ros_domain_id}_{uuid.uuid4().hex}',
        start_parameter_services=False,
        start_type_description_service=False)
    with NetworkAwareNode(node_args) as node:
        functions = [
            node.get_name,
            node.get_namespace,
            node.get_node_names_and_namespaces,
            node.get_node_names_and_namespaces_with_enclaves,
            node.get_topic_names_and_types,
            node.get_service_names_and_types,
            bind(rclpy.action.get_action_names_and_types, node),
            node.get_publisher_names_and_types_by_node,
            node.get_publishers_info_by_topic,
            node.get_subscriber_names_and_types_by_node,
            node.get_subscriptions_info_by_topic,
            node.get_service_names_and_types_by_node,
            node.get_client_names_and_types_by_node,
            bind(rclpy.action.get_action_server_names_and_types_by_node, node),
            bind(rclpy.action.get_action_client_names_and_types_by_node, node),
            node.count_publishers,
            node.count_subscribers,
            node.count_clients,
            node.count_services
        ]

        # Dealing with the timeouts in this server is a bit tricky.  The caller
        # passes in an overall inactivity timeout via the 'timeout' parameter;
        # this server should quit when there is no activity within that timeout.
        # The 'server.timeout' specifies how long 'server.handle_request()'
        # should wait in 'select()' before returning with no work to do.  We set
        # the 'server.timeout' to 200 milliseconds so we will react fairly
        # quickly to external signals and quit.  To deal with the overall
        # timeout, each function that is called resets the timer.  The result
        # of all of this is that we properly react to signals (SIGINT and
        # SIGTERM), we properly timeout when we are idle, and we properly quit
        # when we are told to shutdown.

        last_function_call_time = time.time()

        def reset_timer_and_pretty_print(func, *args, **kwargs):
            nonlocal last_function_call_time
            last_function_call_time = time.time()
            pretty_print_call(func, args, kwargs)

        server.register_introspection_functions()
        for func in functions:
            server.register_function(
                before_invocation(
                    func, reset_timer_and_pretty_print))

        shutdown = False

        def timeout_handler():
            nonlocal shutdown

            if time.time() - last_function_call_time > timeout:
                print('Shutdown due to timeout')
                shutdown = True
        server.handle_timeout = timeout_handler
        server.timeout = 0.2

        # function to shutdown daemon remotely
        def shutdown_handler():
            nonlocal shutdown
            print('Remote shutdown requested')
            shutdown = True
        server.register_function(shutdown_handler, 'system.shutdown')

        print('Serving XML-RPC on ' + get_xmlrpc_server_url(server.server_address))
        try:
            while rclpy.ok() and not shutdown:
                server.handle_request()
        except KeyboardInterrupt:
            pass


def serve_and_close(server: LocalXMLRPCServer, *, timeout: int = 2 * 60 * 60):
    try:
        serve(server, timeout=timeout)
    finally:
        server.server_close()


def main(*, argv=None):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--rmw-implementation', type=str, required=True,
        help='The RMW implementation name (must match the return value of '
             'rclpy.get_rmw_implementation_identifier())')
    parser.add_argument(
        '--ros-domain-id', metavar='N', type=int, required=True,
        help='The ROS domain id (must match the environment variable '
             'ROS_DOMAIN_ID)')
    parser.add_argument(
        '--timeout', metavar='N', type=int, default=2 * 60 * 60,
        help='Shutdown the daemon after N seconds of inactivity')
    args = parser.parse_args(args=argv)

    # the arguments are only passed for visibility in e.g. the process list
    assert args.rmw_implementation == rclpy.get_rmw_implementation_identifier()
    assert args.ros_domain_id == get_ros_domain_id()

    with make_xmlrpc_server() as server:
        serve(server, timeout=args.timeout)


if __name__ == '__main__':
    main()
