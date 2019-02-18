//
// Created by zy234 on 2/18/19.
//
#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <tf2/LinearMath/Quaternion.h>
#include "rviz_pose/att.h"

#define PI 3.1415926

ros::Publisher pose_pub;

void dataCallback(const rviz_pose::att::ConstPtr &msg) {
    //ROS_INFO("roll: %f pitch: %f yaw: %f", msg->roll, msg->pitch, msg->yaw);

    tf2::Quaternion attitude;

    geometry_msgs::PoseStamped pose;
    pose.header.frame_id = "my_drone";
    pose.header.stamp = ros::Time::now();

    attitude.setRPY(PI * msg->roll / 180, PI * msg->pitch / 180, PI * msg->yaw / 180);

    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = 0;
    pose.pose.orientation.x = attitude[0];
    pose.pose.orientation.y = attitude[1];
    pose.pose.orientation.z = attitude[2];
    pose.pose.orientation.w = attitude[3];

    pose_pub.publish(pose);
}


int main(int argc, char **argv) {
    ros::init(argc, argv, "rviz_pose");
    ros::NodeHandle n;

    ros::Subscriber sub = n.subscribe("flightdata", 1000, dataCallback);
    pose_pub = n.advertise<geometry_msgs::PoseStamped>("drone_pose", 1);

    ros::spin();
    return 0;

}

