#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
class hello_ros(Node):

    def __init__(self):
      super().__init__("node1")
      self.counter=0
      self.robo_name="lolita"
      self.create_timer(1.0, self.loop)
      self.ct_pub=self.create_publisher(String,"pub",10)
    def loop(self):
       
        msg=String()
        msg.data="hello this is "+str(self.robo_name)
        self.ct_pub.publish(msg)
        self.counter+=1
    
      
     



def main(args=None):
    rclpy.init(args=args)
    node=hello_ros()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()