# Authors: 
# Erik Berglund
# Adam Fridén Rasmussen
# Date: 2023-02-23
# Based on https://automaticaddison.com/create-a-basic-publisher-and-subscriber-python-ros2-foxy/ as well as 
# https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html


import rclpy
from Sonar import Sonar    
from rw_interfaces.msg import Ultrasonic
from rclpy.node import Node


class Sonar_Publisher(Node):
    def __init__(self):
        super().__init__('Sonar_Publisher')
        #Create publisher that publishes to the topic 'Sonar value' with a queue limit of 10
        self.publisher_ = self.create_publisher(Ultrasonic, 'Sonar_Value', 10)
        # Publish message every 0.5 seconds 
        timer_period = 0.5 
        # A timer that calls the function timer_callback in periods of time_period. 
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # lägg in data från sonar
        sonar = Sonar('COM3', 9600)
        sonarvalue = Ultrasonic()
        sonarvalue.data = sonar.getDistance()
        self.publisher_.publish(sonarvalue) # publicera datan från sonar till topic 'Sonar value' 


def main(args=None):
    rclpy.init(args=args)
    
    sonar_publisher = Sonar_Publisher()

    rclpy.spin(sonar_publisher)

    sonar_publisher.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()