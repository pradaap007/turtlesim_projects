import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen


class box(Node):
    def __init__(self):
        super().__init__("box_turtle")
        self.cmd_vel_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.pose_sub=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
    def pose_callback(self,pose:Pose):
        cmd=Twist()
        if pose.x>9.0 or pose.x <2.0 or pose.y>9.0 or pose.y<2.0:
            cmd.linear.x=1.0
            cmd.angular.z=0.9
        else:
            cmd.linear.x=5.0
            cmd.angular.z=0.0
        print("postion in x",pose.x)  
        print("position in y:",pose.y)  
        print("linear_vel in x:",cmd.linear.x)
        print("angualr_vel in z",cmd.angular.z)
        self.cmd_vel_pub.publish(cmd)
def main(args=None):
    rclpy.init(args=args)
    node=box()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()