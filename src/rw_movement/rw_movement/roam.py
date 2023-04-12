import rclpy
import rclpy.qos
from rclpy.action import ActionClient
from geometry_msgs.msg import Twist
from irobot_create_msgs.msg import HazardDetection, HazardDetectionVector
from irobot_create_msgs.action import RotateAngle
from rclpy.node import Node, QoSProfile
from sensor_msgs.msg import Imu
import time

from rw_interfaces.msg import DetectionsVector, RobotStatus, Ultrasonic


class Roam(Node):
    HAZARD_TIME_INTERVAL = 1
    lastHazardTime = time.time()
    roamMode = False  # True = Roam, False = Avoid
    orientation = 0.0
    hazard_orientation = 0.0
    def __init__(self):
        super().__init__('roam')
        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
                                          depth=1)
        self.get_logger().info("Roam node started")

        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)

        self.hazard_sub = self.create_subscription(
            HazardDetectionVector,
            'hazard_detection',
            self.detection_callback,
            qos_profile=qos_policy
        )
        self.sonar_sub = self.create_subscription(
            Ultrasonic,
            'sonar_value',
            self.sonar_callback,
            qos_profile=qos_policy
        )
        self.behaviour_sub = self.create_subscription(RobotStatus, 'behaviour', self.behaviour_callback, qos_policy)

        self._action_client = ActionClient(self, RotateAngle, 'rotate_angle')

    def imu_callback(self, msg):
        #self.get_logger().info("imu %f" % msg.orientation.z)
        self.orientation = msg.orientation.z

        
    def behaviour_callback(self, msg):
        self.get_logger().info("behaviour")
        self.roamMode = msg.roam

    def sonar_callback(self,msg):
        if not self.roamMode:
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
        if not self.roamMode:
            return
        twist = Twist()
        if (self.isCollisionHazard(msg) and self.cooldownIsDone()):
            self.get_logger().info("Hazard detected")
            self.rotate(3.14)
        elif(RobotStatus == False):
            self.noHazardMovement(twist)
        self.vel_pub.publish(twist)
    
    def cooldownIsDone(self):
        if time.time() - self.lastHazardTime > self.HAZARD_TIME_INTERVAL:
            self.lastHazardTime = time.time()
            return True
        return False

    def isCollisionHazard(self, msg):
        return len(msg.detections) != 0

    def getHazardAvoidance(self, msg, twist):
        twist.linear.x = 0.0
        twist.angular.z = 1.7

    def noHazardMovement(self, twist):
        twist.linear.x = 0.1
        twist.angular.z = 0.0
        
    def rotate(self, radians):
        self._action_client._is_ready 
        goal_msg = RotateAngle.Goal()
        goal_msg.angle = radians

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Rotation complete' + str(result))


def main():
    rclpy.init()
    node = Roam()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()