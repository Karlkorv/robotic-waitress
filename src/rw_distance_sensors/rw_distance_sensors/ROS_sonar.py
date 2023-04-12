# Authors: 
# Erik Berglund
# Adam Fridén Rasmussen
# Date: 2023-02-23
# Based on https://automaticaddison.com/create-a-basic-publisher-and-subscriber-python-ros2-foxy/ as well as 
# https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html


import rclpy
from rw_distance_sensors.Sonar import Sonar
from rw_interfaces.msg import Ultrasonic
from rclpy.node import Node



class Sonar_Publisher(Node):
    def __init__(self):
        super().__init__('Sonar_Publisher')
        #Create publisher that publishes to the topic 'Sonar value' with a queue limit of 10
        self.publisher_ = self.create_publisher(msg_type=Ultrasonic, topic='sonar_value', qos_profile=10)
        # Publish message every 0.5 seconds 
        timer_period = 0.5 
        # A timer that calls the function timer_callback in periods of time_period. 
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # lägg in data från sonar
        collectL = False
        collectC = False
        collectR = False
        sonar = Sonar('/dev/ttyACM0', 9600)
        sonarvalue = Ultrasonic()
        while(True):
            result = sonar.getDistance()
            if result is not None:
                if result[0] == 'L' and not collectL:
                    sonarvalue.distances[0] = float(result[1:])
                    collectL = True
                elif result[0] == 'C' and not collectC:
                    sonarvalue.distances[1] = float(result[1:])
                    collectC = True
                elif result[0] == 'R' and not collectR:
                    sonarvalue.distances[2] = float(result[1:])
                    collectR = True
                else:
                    continue

            """ match result[0]:
                case 'L':
                    if not collectL:
                        sonarvalue[0] = float(result[1:])
                        collectL = True
                case 'C':
                    if not collectC:
                        sonarvalue[1] = float(result[1:])
                        collectC = True
                case 'R':
                    if not collectR:
                        sonarvalue[2] = float(result[1:])
                        collectR = True
                case _: 
                    continue """
            if(collectL and collectC and collectR):
                sonar.closePort()
                break
        
        # det behövs ngn kontroll så att det måste vara en L, en C och en R
        self.get_logger().info("[left '%f', center: '%f', right: '%f']" % (sonarvalue.distances[0], sonarvalue.distances[1], sonarvalue.distances[2]))
        self.publisher_.publish(sonarvalue) # publicera datan från sonar till topic 'Sonar value' 


def main(args=None):
    rclpy.init(args=args)
    
    sonar_publisher = Sonar_Publisher()

    rclpy.spin(sonar_publisher)

    sonar_publisher.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()