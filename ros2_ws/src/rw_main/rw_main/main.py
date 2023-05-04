import rclpy
import rclpy.qos
from rclpy.node import Node
from rw_interfaces.msg import RobotStatus
from std_msgs.msg import Bool
# TODO: Vi kan inte få tag på roam-noden, fixa importer + inter-package dependencies
class Main(Node):
    def __init__(self):
        super().__init__('main')
        self.get_logger().info("Main node started")
        self.behaviour_pub = self.create_publisher(RobotStatus, 'behaviour', 10)
        self.human_sub = self.create_subscription(
            Bool,
            'human_detection',
            self.human_callback,
            10
        )
        self.screen_sub = self.create_subscription(
            Bool,
            'touchscreen_feedback',
            self.human_callback,
            10
        )
    
    def human_callback(self, msg):
        self.get_logger().info("Human detection callback")
        if msg.isHumanDetected:
            behaviour = RobotStatus()
            behaviour.roam = False
            self.behaviour_pub.publish(behaviour)

    def screen_callback(self, msg):
        self.get_logger().info("Screen callback")
        behaviour= RobotStatus()
        if msg.hasBeenTouched:
            behaviour.roam = False 
            self.behaviour_pub.publish(behaviour)
        elif msg.isConversationEnded:
            behaviour.roam = True
            self.behaviour_pub.publish(behaviour)

def main():
    rclpy.init()
    main = Main()
    rclpy.spin(main)
    rclpy.shutdown()


if __name__ == '__main__':
    main()