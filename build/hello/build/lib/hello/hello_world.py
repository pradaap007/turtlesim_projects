#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class hello_ros(Node):

    def __init__(self):
      super().__init__("node1")
      self.create_timer(1.0 ,self.timer())
    def timer(self):
        self.get_logger().info("hello boss")




def main(args=None):
    rclpy.init(args=args)
    node=hello_ros()
    rclpy.shutdown


if __name__=="__main__":
    main()