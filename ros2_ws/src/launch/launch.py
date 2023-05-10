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
            package='rw_sensors',
            executable='camera',
            name='camera'
        ),
        # Node(
        #     package='rw_screen',
        #     executable='gui',
        #     name='gui'
        # ),
    ])