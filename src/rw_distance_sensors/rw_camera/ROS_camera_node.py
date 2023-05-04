#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from rw_camera import Human
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
        # A timer that calls the function timer_callback in periods of time_period. 
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # lägg in data från Human
        sensor = Human() # Skapa instans av klassen Human.
        sonarvalue = Ultrasonic() # Message type
        sonarvalue.distance =  1 # Hämta bool value från human.
        self.get_logger().info('Sonar value: "%f"' % sonarvalue.distance)
        self.publisher_.publish(sonarvalue) # publicera datan från sonar till topic 'Sonar value'