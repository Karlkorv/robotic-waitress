#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from rw_camera import Human
from rw_interfaces.msg import HumanDetection
import cv2
#den här nedanför ska bytas ut till motsvarande för kameran
#from rw_distance_sensors.Sonar import Sonar
#from rw_interfaces.msg import Ultrasonic


class Camera_Publisher(Node):
    def __init__(self):
        super().__init__('Camera_Publisher')
        #Create publisher that publishes to the topic 'human_detection' with a queue limit of 10
        self.publisher_ = self.create_publisher(msg_type=Bool, topic='human_detection', qos_profile=10)
        # Publish message every 1 seconds 
        timer_period = 1
        model = "efficientdet_lite0.tflite"
        camera_id = 0
        width = 640
        height = 480
        num_threads = 4
        enable_edgetpu = False
        detector = Human(model, camera_id, width, height, num_threads, enable_edgetpu)
        camera = cv2.VideoCapture(camera_id)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        # A timer that calls the function timer_callback in periods of time_period. 
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # lägg in data från Human
        tfDetection = HumanDetection() # Message type
        tfDetection.foundHuman =  self.detector.detectHuman(self.camera) # Hämta bool value från human.
        self.publisher_.publish(tfDetection) # publicera datan från sonar till topic 'Sonar value'

def main(args=None):
    rclpy.init(args=args)
    camera_publisher = Camera_Publisher()
    rclpy.spin(camera_publisher)
    camera_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()