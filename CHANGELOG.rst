^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ros2action
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.9.13 (2023-03-16)
-------------------
* Added changelogs
* Contributors: Dharini Dutia

0.9.12 (2022-09-12)
-------------------

0.9.11 (2022-01-31)
-------------------

0.9.10 (2021-10-05)
-------------------

0.9.9 (2021-03-24)
------------------
* 0.9.9
* Contributors: Audrow Nash

0.9.8 (2020-12-08)
------------------

0.9.7 (2020-07-07)
------------------

0.9.6 (2020-06-23)
------------------

0.9.5 (2020-06-01)
------------------

0.9.4 (2020-05-26)
------------------

0.9.3 (2020-05-13)
------------------
* Make CLI more robust to discovery latency. (`#494 <https://github.com/ros2/ros2cli/issues/494>`_)
* Contributors: Michel Hidalgo

0.9.2 (2020-05-08)
------------------

0.9.1 (2020-05-06)
------------------

0.9.0 (2020-04-29)
------------------
* Skip CLI tests on Windows until we resolve the blocking/hanging isuse. (`#489 <https://github.com/ros2/ros2cli/issues/489>`_)
* more verbose test_flake8 error messages (same as `ros2/launch_ros#135 <https://github.com/ros2/launch_ros/issues/135>`_)
* Remove ready_fn from test descriptions (`#376 <https://github.com/ros2/ros2cli/issues/376>`_)
* used get_available_rmw_implementations from rclpy (`#461 <https://github.com/ros2/ros2cli/issues/461>`_)
* Add delay when retrying tests involving the CLI daemon (`#459 <https://github.com/ros2/ros2cli/issues/459>`_)
* use f-string (`#448 <https://github.com/ros2/ros2cli/issues/448>`_)
* only load required entry points which improves the performance (`#436 <https://github.com/ros2/ros2cli/issues/436>`_)
* [ros2action] Refactor send_goal implementation (`#406 <https://github.com/ros2/ros2cli/issues/406>`_)
* Merge branch 'master' of github.com:ros2/ros2cli
* [ros2action] Remove show verb (`#405 <https://github.com/ros2/ros2cli/issues/405>`_)
* Contributors: Alejandro Hernández Cordero, Dirk Thomas, Jacob Perron, Peter Baughman, Steven! Ragnarök, claireyywang

0.8.6 (2019-11-19)
------------------
* fix new linter warnings as of flake8-comprehensions 3.1.0 (`#399 <https://github.com/ros2/ros2cli/issues/399>`_)
* Contributors: Dirk Thomas

0.8.5 (2019-11-14)
------------------
* 0.8.5
* Contributors: Shane Loretz

0.8.4 (2019-11-13)
------------------
* 0.8.4
* Contributors: Michael Carroll

0.8.3 (2019-10-23)
------------------
* 0.8.3
* End-to-end test coverage for CLI commands output (`#304 <https://github.com/ros2/ros2cli/issues/304>`_)
* ensure ros2 interface show has trailing newline (`#368 <https://github.com/ros2/ros2cli/issues/368>`_)
* Contributors: Dirk Thomas, Michel Hidalgo, Shane Loretz

0.8.2 (2019-10-08)
------------------
* 0.8.2
* Contributors: Dirk Thomas

0.8.1 (2019-10-04)
------------------
* 0.8.1
* Contributors: Michael Carroll

0.8.0 (2019-09-26)
------------------
* install resource marker file for packages (`#339 <https://github.com/ros2/ros2cli/issues/339>`_)
* Update setup.py version (`#331 <https://github.com/ros2/ros2cli/issues/331>`_)
* install package manifest (`#330 <https://github.com/ros2/ros2cli/issues/330>`_)
* Pass keyword arguments by name (`#317 <https://github.com/ros2/ros2cli/issues/317>`_)
* Add action send_goal prototype completer (`#301 <https://github.com/ros2/ros2cli/issues/301>`_)
* Contributors: Dirk Thomas, Jacob Perron, Jeremie Deray

0.7.4 (2019-05-29)
------------------
* [ros2action] Support multiple part action type names for 'send_goal' verb (`#261 <https://github.com/ros2/ros2cli/issues/261>`_)
* use three-part interface names in msg/srv/action show and msg/srv/ list (`#259 <https://github.com/ros2/ros2cli/issues/259>`_)
* reset goal_handle to avoid attempt to cancel (`#254 <https://github.com/ros2/ros2cli/issues/254>`_)
* Contributors: Dirk Thomas, Jacob Perron

0.7.3 (2019-05-20)
------------------

0.7.2 (2019-05-08)
------------------
* add xmllint linter test (`#232 <https://github.com/ros2/ros2cli/issues/232>`_)
* use yaml.safe_load (round2) (`#229 <https://github.com/ros2/ros2cli/issues/229>`_)
* Contributors: Mikael Arguedas

0.7.1 (2019-04-17)
------------------

0.7.0 (2019-04-14)
------------------
* Add Action CLI (`#214 <https://github.com/ros2/ros2cli/issues/214>`_)
* Contributors: Jacob Perron

0.6.3 (2019-02-08)
------------------

0.6.2 (2018-12-12)
------------------

0.6.1 (2018-12-06)
------------------

0.6.0 (2018-11-19)
------------------

0.5.4 (2018-08-20)
------------------

0.5.3 (2018-07-17)
------------------

0.5.2 (2018-06-28)
------------------

0.5.1 (2018-06-27 12:27)
------------------------

0.5.0 (2018-06-27 12:17)
------------------------

0.4.0 (2017-12-08)
------------------
