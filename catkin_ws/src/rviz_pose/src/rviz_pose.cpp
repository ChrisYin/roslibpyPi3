#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <tf2/LinearMath/Quaternion.h>

#define PI 3.1415926

int main(int argc, char **argv) {
    ros::init(argc, argv, "rviz_pose");
    ros::NodeHandle n;
    ros::Rate r(1);
    ros::Publisher pose_pub = n.advertise<geometry_msgs::PoseStamped>("drone_pose", 1);


    tf2::Quaternion attitude;
    float att[3] = {0, 0, 0};

    while (ros::ok()) {
        geometry_msgs::PoseStamped pose;
        pose.header.frame_id = "my_drone";
        pose.header.stamp = ros::Time::now();

// Create this quaternion from roll/pitch/yaw (in radians)
        attitude.setRPY(PI * att[0] / 180, PI * att[1] / 180,
                        PI * att[2] / 180);

        pose.pose.position.x = 0;
        pose.pose.position.y = 0;
        pose.pose.position.z = 0;
        pose.pose.orientation.x = attitude[0];
        pose.pose.orientation.y = attitude[1];
        pose.pose.orientation.z = attitude[2];
        pose.pose.orientation.w = attitude[3];

        while (pose_pub.getNumSubscribers() < 1) {
            if (!ros::ok()) {
                return 0;
            }
            ROS_WARN_ONCE("Please create a subscriber to the marker");
            sleep(1);
        }

        pose_pub.publish(pose);
        att[1] += 20;
        att[2] += 10;

        r.sleep();

    }

    return 0;

}
