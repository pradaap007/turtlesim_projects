#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
class sub(Node):
    def __init__(self):
        super().__init__("sub1")
        self.subs=self.create_subscription(String,"pub",self.call_back,10)
        

    def call_back(self,msg):
        self.get_logger().info(msg.data)




def main(args=None):
    rclpy.init(args=args)
    node=sub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()