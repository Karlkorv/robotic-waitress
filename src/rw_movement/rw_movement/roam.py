import rclpy
import rclpy.qos
from rclpy.node import Node
from rclpy.node import QoSProfile
from geometry_msgs.msg import Twist
from irobot_create_msgs.msg import HazardDetectionVector, HazardDetection

class Roam(node):

    def __init__(self):
        super().__init__('roam')
        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
                                            depth=1)
        self.get_logger().info("Roam node started")
        
        self.hazard_sub = self.create_subscription(
            HazardDetectionVector,
            'hazard_detection',
            self.hazard_callback,
            qos_profile=qos_policy
            )