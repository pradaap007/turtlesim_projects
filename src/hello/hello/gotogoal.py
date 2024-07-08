import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import sys
class gtg(Node):
    def __init__(self):
        super().__init__("go_to_goal")
        self.cmd_vel_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.pose_sub=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.create_timer(0.5,self.movement)
        self.data=None
    def pose_callback(self, data):
        self.data=data

    def movement(self):
        pose=Pose()
        pose.x=float(sys.argv[1])
        pose.y=float(sys.argv[2])
        pose.theta=float(sys.argv[3])
        vel=Twist()
        gtg=math.sqrt((pose.x-self.data.x)**2 + (pose.y-self.data.y)**2)
        atg=math.atan2(pose.y-self.data.y,pose.x-self.data.x)
        dis_tol=0.01
        ang_tol=0.01
        ang_to_go=atg-self.data.theta
        kp =2
        if abs(ang_to_go)>ang_tol:
            vel.angular.z=kp*ang_to_go
        else:
            if (gtg)>=dis_tol:
                vel.linear.x=kp*gtg
            else:
                vel.linear.x=0.0
                self.get_logger().info("goal reached")
                quit()
        self.cmd_vel_pub.publish(vel)
def main(args=None):
    rclpy.init(args=args)
    node=gtg()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()