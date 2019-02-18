source catkin_ws/devel/setup.bash
roscore&
sleep 2
roslaunch rosbridge_server rosbridge_websocket.launch&
rosrun flightdata flghtDataListener.py&
rosrun rviz_pose rviz_pose&
rosrun rviz rviz
