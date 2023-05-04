import rclpy
import rclpy.qos
from geometry_msgs.msg import Twist
from irobot_create_msgs.msg import HazardDetection, HazardDetectionVector
from rclpy.node import Node, QoSProfile
from sensor_msgs.msg import Imu

from rw_interfaces.msg import DetectionsVector, RobotStatus, Ultrasonic


class Roam(Node):
    robotStatus = False  # True = Roam, False = Avoid
    orientation = 0.0
    hazard_orientation = 0.0
    def __init__(self):
        super().__init__('roam')
        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
                                          depth=1)
        self.get_logger().info("Roam node started")

        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)

        # self.hazard_sub = self.create_subscription(
        #     HazardDetectionVector,
        #     'hazard_detection',
        #     self.detection_callback,
        #     qos_profile=qos_policy
        # )
        self.sonar_sub = self.create_subscription(
            Ultrasonic,
            'sonar_value',
            self.sonar_callback,
            qos_profile=qos_policy
        )
        self.imu_sub = self.create_subscription(Imu, 'imu', self.imu_callback, qos_policy)
        self.behaviour_sub = self.create_subscription(RobotStatus, 'behaviour', self.behaviour_callback, qos_policy)

    def imu_callback(self, msg):
        #self.get_logger().info("imu %f" % msg.orientation.z)
        self.orientation = msg.orientation.z

        
    def behaviour_callback(self, msg):
        self.get_logger().info("behaviour")
        self.robotStatus = msg.roam

    def sonar_callback(self,msg):
        if not self.robotStatus:
            return
        twist = Twist()
        if self.hazard_orientation+0.5 < self.orientation:
            twist.linear.x = 0.0
            twist.angular.z = 1.0
            self.vel_pub.publish(twist)
            return
        if msg.distance < 40:
            self.hazard_orientation = self.orientation
        else:
            twist.linear.x = 0.1
            twist.angular.z = 0.0
        self.get_logger().info("%f" % self.orientation)
        self.vel_pub.publish(twist)


    def detection_callback(self, msg):
        if not self.robotStatus:
            return
        self.get_logger().info("Hazard detected")
        twist = Twist()
        if (self.isCollisionHazard(msg)):
            self.getHazardAvoidance(msg, twist)
        elif(RobotStatus == False):
            self.noHazardMovement(twist)
        self.vel_pub.publish(twist)
    
    def isCollisionHazard(self, msg):
        return len(msg.detections) != 0

    def getHazardAvoidance(self, msg, twist):
        twist.linear.x = 0.0
        twist.angular.z = 1.7

    def noHazardMovement(self, twist):
        twist.linear.x = 0.1
        twist.angular.z = 0.0


def main():
    rclpy.init()
    node = Roam()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
