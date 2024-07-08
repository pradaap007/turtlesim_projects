#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
class circle(Node):
    def __init__(self):
        super().__init__("circle")
        self.cmd_vel_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_timer(0.5,self.turtle)
        self.get_logger().info("hey turtle make a circle")
    def turtle(self):
        linear_vel=float(sys.argv[1])
        radius=float(sys.argv[2])
        tur= Twist()
        tur.linear.x=linear_vel
        tur.angular.z=linear_vel/radius
        self.cmd_vel_pub.publish(tur)

    
def main(args=None):
    rclpy.init(args=args)
    node=circle()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()