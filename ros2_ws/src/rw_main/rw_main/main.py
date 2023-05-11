import rclpy
import rclpy.qos
from rclpy.node import Node
from rw_interfaces.msg import RobotStatus, DisplayStatus, HumanDetection # type: ignore
from std_msgs.msg import Bool, Header
from builtin_interfaces.msg import Time
import sys
# TODO: Vi kan inte få tag på roam-noden, fixa importer + inter-package dependencies
class Main(Node):
    def __init__(self):
        super().__init__('main') # type: ignore
        self.get_logger().info("Main node started")
        self.lastConv = self.get_clock().now().to_msg().sec
        self.lastTouch = 2**32-1
        self.in_conversation = False
        self.behaviour_pub = self.create_publisher(RobotStatus, 'behaviour', 10)
        self.camera_pub = self.create_publisher(Bool, 'camera_enabled', 10)
        self.human_sub = self.create_subscription(
            HumanDetection,
            'human_detection',
            self.human_callback,
            0
        )
        self.screen_sub = self.create_subscription(
            DisplayStatus,
            'touchscreen_feedback',
            self.screen_callback,
            10
        )
        self.timer = self.create_timer(0.1, self.timer_callback)

    def human_callback(self, msg: HumanDetection) -> None:
        PROBABILITY_THRESHOLD = 0.80
        self.get_logger().info(f"{self.lastConv}, now: {self.get_clock().now().to_msg().sec}")
        if msg.probability > PROBABILITY_THRESHOLD:
            behaviour = RobotStatus()
            self.get_logger().info("Human detected")
            behaviour.roam = False
            camera_msg = Bool()
            camera_msg.data = False
            self.camera_pub.publish(camera_msg)
            self.behaviour_pub.publish(behaviour)
    
    def screen_callback(self, msg: DisplayStatus) -> None:
        #self.get_logger().info(f"Screen callback {msg._in_conversation} {msg.header.stamp.sec}")
        self.in_conversation = msg.in_conversation
        self.lastTouch = msg.header.stamp.sec
        if not msg.in_conversation:
            self.lastConv = msg.header.stamp.sec
            self.lastTouch = 0
            behaviour = RobotStatus()
            behaviour.roam = True
            self.behaviour_pub.publish(behaviour)

    def timer_callback(self) -> None:
        TIMER_THRESHOLD = 10
        #self.get_logger().info(f"lastConv: {self.lastConv}, lastTouch: {self.lastTouch}, now: {self.get_clock().now().to_msg().sec}")
        if self.get_clock().now().to_msg().sec - self.lastConv > TIMER_THRESHOLD and not self.in_conversation:
            #self.get_logger().info(f"{self.get_clock().now().to_msg().sec - self.lastConv}")
            behaviour = RobotStatus()
            behaviour.roam = True
            self.behaviour_pub.publish(behaviour)
            camera_msg = Bool()
            camera_msg.data = True
            self.camera_pub.publish(camera_msg)
        LAST_TOUCH_THRESHOLD = 30
        self.get_logger().info(f"lasttouch: {self.get_clock().now().to_msg().sec - self.lastTouch}")
        if self.get_clock().now().to_msg().sec - self.lastTouch > LAST_TOUCH_THRESHOLD:
            self.lastTouch = 2**32-1
            behaviour = RobotStatus()
            behaviour.roam = True
            self.behaviour_pub.publish(behaviour)
            

            


def main():
    rclpy.init()
    main = Main()
    rclpy.spin(main)
    rclpy.shutdown()


if __name__ == '__main__':
    main()