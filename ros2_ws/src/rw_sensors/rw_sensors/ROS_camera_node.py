#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from rw_interfaces.msg import HumanDetection, Displaystatus
from multiprocessing.connection import Client
#den här nedanför ska bytas ut till motsvarande för kameran
#from rw_distance_sensors.Sonar import Sonar
#from rw_interfaces.msg import Ultrasonic


class Camera_Publisher(Node):
    """
    A ROS2 node that publishes human detection messages based on data received
    from a server over a socket connection. All the detection logic is in detect2.py.

    Attributes:
        publisher_ (Publisher): A publisher that sends messages of type `HumanDetection`
                                to the 'human_detection' topic.
        timer (Timer): A timer that periodically triggers the `timer_callback` method.
    """
    in_conversation = False
    def __init__(self):
        """
        Initializes the Camera_Publisher node, sets up the publisher, and starts the timer.
        """
        super().__init__('Camera_Publisher')
        #Create publisher that publishes to the topic 'human_detection' with a queue limit of 10
        self.publisher_ = self.create_publisher(msg_type=HumanDetection, topic='human_detection', qos_profile=10)
        self.touchscreen_sub = self.create_subscription(
            msg_type=Displaystatus, 
            topic='touchscreen_feedback', 
            callback=self.touchscreen_callback, 
            qos_profile=10)
        # Publish message every 1 seconds 
        timer_period = 0.5
        # A timer that calls the function timer_callback in periods of time_period. 
        
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def touchscreen_callback(self, msg: Displaystatus) -> None:
        self.in_conversation = msg.in_conversation
            


    def timer_callback(self) -> None:
        """
        Attempts to connect to the server, receive data, and publish the
        received value as a HumanDetection message. Logs an info message if the
        connection is refused.
        """
        if self.in_conversation:
            return
        try:
            with Client(('localhost', 5000)) as conn:
                value = conn.recv()
                self.get_logger().info(f"{value}")
                msg = HumanDetection()
                msg.probability = float(value)
                self.publisher_.publish(msg)
                conn.close()
        except ConnectionRefusedError:
            self.get_logger().info("Connection refused, starta detect2.py")

def main(args=None):
    rclpy.init(args=args)
    camera_publisher = Camera_Publisher()
    rclpy.spin(camera_publisher)
    camera_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()