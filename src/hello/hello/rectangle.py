#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


import math

class MoveSquareServer(Node):

    def __init__(self):
        super().__init__('move_square_server')
        self.srv = self.create_service(MoveSquare, 'move_square', self.handle_move_square)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.speed = 3.0  # Default speed
        self.PI = math.pi

    def handle_move_square(self, request, response):
        self.get_logger().info('Executing move_square request')
        side_length = request.s
        rotations = request.r

        current_rotation = 0
        while current_rotation < rotations:
            self.move_in_line(side_length)
            self.rotate()
            current_rotation += 0.25

        response.success = True
        return response

    def move_in_line(self, side_length):
        vel_msg = Twist()
        vel_msg.linear.x = self.speed
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        distance_travelled = 0
        t0 = self.get_clock().now()

        while distance_travelled < side_length:
            self.publisher.publish(vel_msg)
            t1 = self.get_clock().now()
            distance_travelled = self.speed * (t1 - t0).nanoseconds / 1e9

        vel_msg.linear.x = 0
        self.publisher.publish(vel_msg)

    def rotate(self):
        vel_msg = Twist()
        angular_speed = 2
        vel_msg.angular.z = angular_speed

        angle_travelled = 0
        t0 = self.get_clock().now()

        while angle_travelled < self.PI / 2.0:
            self.publisher.publish(vel_msg)
            t1 = self.get_clock().now()
            angle_travelled = angular_speed * (t1 - t0).nanoseconds / 1e9

        vel_msg.angular.z = 0
        self.publisher.publish(vel_msg)


def main(args=None):
    rclpy.init(args=args)
    move_square_server = MoveSquareServer()
    rclpy.spin(move_square_server)
    move_square_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
