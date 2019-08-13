#!/usr/bin/env python

from go_to_goal.srv import *
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
class TurtleBot:
    
    
    def __init__(self): 
        
        rospy.init_node('turtlebot_controller', anonymous=True)

        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)
    

    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    
    def euclidean_distance(self, goal_pose):
        return sqrt((pow(goal_pose.x - self.pose.x, 2) + pow(goal_pose.y - self.pose.y, 2)))


    def linear_vel(self, goal_pose, k):
        return k * self.euclidean_distance(goal_pose)


    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)


    def angular_vel(self, goal_pose, k):
        return k * (self.steering_angle(goal_pose) - self.pose.theta)


    def handle(self, req):
        if req.x >= 0 and req.y >= 0:
            print "Valid coodinates!"
            
            goal_pose = Pose()

            goal_pose.x = req.x
            goal_pose.y = req.y

            distance_tolerance = req.tollerance

            vel_msg = Twist()

            while self.euclidean_distance(goal_pose) >= distance_tolerance:

                constantK = rospy.get_param('/go/constantK')
                constantT = rospy.get_param('/go/constantT')

                vel_msg.linear.x = self.linear_vel(goal_pose, constantK)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel(goal_pose, constantT)

                self.velocity_publisher.publish(vel_msg)

                self.rate.sleep()

            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)

            return GoalResponse(True)
        else:
            print "Invalid coordinates!"
            return GoalResponse(False)

    def goal_coordinates_server(self): 
        print "Server running"

        s = rospy.Service('goal_coordinates', Goal, self.handle)

        rospy.spin()


if __name__ == "__main__":
    x = TurtleBot()
    x.goal_coordinates_server()