from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rw_main',
            executable='main',
            name='main'
        ),
        Node(
            package='rw_movement',
            executable='roam',
            name='roam'
        ),
        Node(
            package='rw_distance_sensors',
            executable='sonar',
            name='sonar'
        )
    ])