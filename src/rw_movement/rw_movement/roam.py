import rclpy
import rclpy.qos
from rclpy.node import Node
from rclpy.node import QoSProfile
from geometry_msgs.msg import Twist
from irobot_create_msgs.msg import HazardDetectionVector, HazardDetection
from rw_interfaces.msg import DetectionsVector, RobotStatus


class Roam(Node):
    robotStatus = False
    def __init__(self):
        super().__init__('roam')
        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
                                          depth=1)
        self.get_logger().info("Roam node started")

        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)

        self.hazard_sub = self.create_subscription(
            DetectionsVector,
            'obstacle_detection',
            self.detection_callback,
            qos_profile=qos_policy
        )
        self.behaviour_sub = self.create_subscription(RobotStatus, 'behaviour', self.behaviour_callback, 10)
        
    def behaviour_callback(self, msg):
        self.get_logger().info(msg)
        self.robotStatus = msg.roam

    def detection_callback(self, msg):
        self.get_logger().info("Hazard detected")
        twist = Twist()
        if (self.isCollisionHazard(msg) and self.robotStatus == False):
            self.get_logger().info(msg.detections[0].frame_id)
            self.getHazardAvoidance(msg, twist)
        elif(RobotStatus == False):
            self.noHazardMovement(twist)
        self.vel_pub.publish(twist)
    
    def isCollisionHazard(msg):
        return len(msg.HazardDetection.detections) != 0 and msg.HazardDetection.detections[0] == 1

    def getHazardAvoidance(msg, twist):
        twist.linear.x = 0.0
        twist.angular.z = 1.7

    def noHazardMovement(twist):
        twist.linear.x = 0.1
        twist.angular.z = 0.0


def main():
    rclpy.init()
    node = Roam()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
