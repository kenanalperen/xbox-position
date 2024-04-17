#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Point, Quaternion

class JoyNode(Node):
    def __init__(self):
        super().__init__("joy_reader")

        self.subscription = self.create_subscription(
            Point,
            '/user_input_position',
            self.listener_callback,
            10
        )
        self.publisher_ = self.create_publisher(PoseStamped, '/franka_a/cartesian_impedance_controller/equilibrium_pose', 10)

    def listener_callback(self, msg):
        # Fixed rotation
        rotation = Quaternion()
        rotation.x = 1.0
        rotation.y = rotation.z = rotation.w = 0.0

        # User input position
        x = msg.x
        y = msg.y
        z = msg.z

        pose_msg = PoseStamped()
        pose_msg.pose.position.x = x
        pose_msg.pose.position.y = y
        pose_msg.pose.position.z = z
        pose_msg.pose.orientation = rotation

        self.publisher_.publish(pose_msg)


def main(args=None):
    rclpy.init(args=args)
    node = JoyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
