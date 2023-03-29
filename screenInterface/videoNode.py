#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class publishNode(Node):

    def __init__(self):
        super().__init__("publish_test")
        self.pub_ = self.create_publisher(String, "/chatter", 10)
        self.timer_ = self.create_timer(5, self.send_command)
        self.get_logger().info("Start publish_test")

    def send_command(self):
        msg = String()
        msg.data = "Start"
        self.pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = publishNode()
    rclpy.spin(node)
    rclpy.shutdown()
