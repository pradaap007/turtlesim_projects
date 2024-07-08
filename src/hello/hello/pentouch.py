import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from functools import partial

class box(Node):
    def __init__(self):
        super().__init__("box_turtle")
        self.prv_x=0
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
        if pose.x>5.5 and self.prv_x<5.5:
            self.prv_x=pose.x
            self.pen_callback(255,0,0,3,0)
        elif pose.x<=5.5 and self.prv_x>=5.5:
            self.prv_x=pose.x
            self.pen_callback(0,255,0,3,0)
    def pen_callback(self,r,b,g,width,off):
        clt=self.create_client(SetPen,"/turtle1/set_pen")
        while not clt.wait_for_service(1.0):
            self.get_logger().warn("waiting for service...")
        rqst=SetPen.Request()
        rqst.r=r
        rqst.b=b
        rqst.g=g
        rqst.width=width
        rqst.off=off
        future=clt.call_async(rqst)
        future.add_done_callback(partial(self.call_pen))
    def call_pen(self,future):
        try:
            res=future.result()
        
        except Exception as e:
            self.get_logger().error("service error: %r"%(e,))

def main(args=None):
    rclpy.init(args=args)
    node=box()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()