import rclpy
import rclpy.qos
from rclpy.action import ActionClient
from geometry_msgs.msg import Twist
from irobot_create_msgs.msg import HazardDetection, HazardDetectionVector
from irobot_create_msgs.action import RotateAngle
from rclpy.node import Node, QoSProfile
from nav_msgs.msg import Odometry
import time
import transforms3d as t3d
import math
import numpy as np

from rw_interfaces.msg import DetectionsVector, RobotStatus, Ultrasonic


class Roam(Node):
    HAZARD_TIME_INTERVAL = 1
    lastHazardTime = time.time()
    roamMode = False 
    hazard = False
    orientation = 0.0
    hazard_orientation = 0.0
    qz= 0.0
    yaw = 0.0
    first_rot_call = True
    target = -1
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

        self.odom_sub = self.create_subscription(Odometry, 'odom', self.odom_callback, qos_policy)

        self.timer = self.create_timer(0.1, self.timer_callback)

    def odom_callback(self, odom_msg: Odometry) -> None:
        self.yaw = get_angle_from_pose(odom_msg.pose.pose)

    def timer_callback(self) -> None:
        if not self.roamMode:
            return 
        #self.get_logger().info("roam")
        if self.hazard:
            self.get_logger().info("hazard")
            self.hazardAvoidance()
        #self.noHazardMovement()     
        
    def behaviour_callback(self, msg: RobotStatus) -> None:
        self.get_logger().info("behaviour")
        self.roamMode = msg.roam

    def sonar_callback(self,msg: Ultrasonic) -> None:
        if not self.roamMode:
            return
        if msg and self.cooldownIsDone(): # TODO om alla avstånd i sonar arrayen är mindre än ett visst avstånd
            self.get_logger().info("Sonar hazard detected")
            self.hazard = True

    def detection_callback(self, msg: HazardDetectionVector) -> None:
        if not self.roamMode:
            return
        if (self.isCollisionHazard(msg) and self.cooldownIsDone()):
            self.get_logger().info("Collision hazard detected")
            self.hazard = True
            

    def isCollisionHazard(self, msg: HazardDetectionVector) -> bool:
        return len(msg.detections) != 0

    def hazardAvoidance(self) -> None:
        temp = 90
        self.rotate(temp)
        self.get_logger().info("hazard avoidance done")
    def noHazardMovement(self) -> None:
        self.get_logger().info("no hazard")
        twist = Twist()
        twist.linear.x = 0.1
        twist.angular.z = 0.0
        self.vel_pub.publish(twist)

    def rotate(self, degrees: float) -> None:
        radians = math.radians(degrees)
        kp = 0.5
        twist = Twist()
        twist.linear.x = 0.0
        if self.first_rot_call:
            self.target = self.yaw + radians
            if self.target > math.pi:
                self.target = self.target -  2*math.pi
            if self.target < -math.pi:
                self.target = self.target + 2*math.pi
            self.first_rot_call = False
        twist.angular.z = kp * (self.target - self.yaw)
        self.vel_pub.publish(twist)
        self.get_logger().info("target:" + str(self.target) + " yaw:" + str(self.yaw) + " diff:" + str(abs(self.target - self.yaw)))
        if abs(self.target - self.yaw) < 0.02:
            self.first_rot_call = True
            self.hazard = False
            self.get_logger().info("Rotation complete")

    def cooldownIsDone(self):
        if time.time() - self.lastHazardTime > self.HAZARD_TIME_INTERVAL:
            self.lastHazardTime = time.time()
            return True
        #self.get_logger().info(str(time.time() - self.lastHazardTime))
        return False

def euler_from_quaternion(quaternion):
    """
    Converts quaternion (w in last place) to euler roll, pitch, yaw
    quaternion = [x, y, z, w]
    Bellow should be replaced when porting for ROS 2 Python tf_conversions is done.
    """
    x = quaternion[0]
    y = quaternion[1]
    z = quaternion[2]
    w = quaternion[3]

    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = np.arctan2(sinr_cosp, cosr_cosp)

    sinp = 2 * (w * y - z * x)
    pitch = np.arcsin(sinp)

    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = np.arctan2(siny_cosp, cosy_cosp)

    return roll, pitch, yaw

def get_angle_from_pose(pose):
    orient_list = [pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w]
    (roll,pitch,yaw) = euler_from_quaternion(orient_list)

    return yaw


def main():
    rclpy.init()
    node = Roam()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

# Helper methods