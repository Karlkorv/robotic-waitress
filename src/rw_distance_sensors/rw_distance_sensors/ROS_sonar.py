# Authors: 
# Erik Berglund
# Adam Fridén Rasmussen
# Date: 2023-05-04
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
        timer_period = 0.1 
        # A timer that calls the function timer_callback in periods of time_period. 
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # initalise new sonar on the port where the arduino is connected
        sonar = Sonar('/dev/ttyACM0', 9600)
        sonarvalue = Ultrasonic()

        distance = sonar.getDistance()
        filteredValues = self.filterValues(distance)
        if(filteredValues == None):
            return
        sonarvalue.distances = filteredValues
        self.get_logger().info("[left: '%f', center: '%f', right: '%f']" % (sonarvalue.distances[0], sonarvalue.distances[1], sonarvalue.distances[2]))
        self.publisher_.publish(sonarvalue) # Publish sonar data to the ROS topic 'Sonar value'
        
        
    """ 
    Ensures there are 3 returned values within reasonable distance limits.
    returns an array of floats with the distances 
    """
    def filterValues(self, sonarDistance):    
            if(sonarDistance == None or sonarDistance == ''):
                return 
            distance_values = sonarDistance.split(",")
            if len(distance_values) != 3:
                return 
            for i in range(len(distance_values)):
                try:
                    if(float(distance_values[i]) > 400):
                        distance_values[i] = 400
                    elif(float(distance_values[i]) < 2):
                        distance_values[i] = 2
                    elif(distance_values[i] == ''):
                        return None
                except ValueError:
                    return None

            return [float(v) for v in distance_values]
        
        
    




def main(args=None):
    rclpy.init(args=args)
    
    sonar_publisher = Sonar_Publisher()

    rclpy.spin(sonar_publisher)

    sonar_publisher.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()