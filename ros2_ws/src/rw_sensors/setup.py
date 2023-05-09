from setuptools import setup

package_name = 'rw_sensors'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gake',
    maintainer_email='gustavakerstrom@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sonar = rw_sensors.ROS_sonar:main',
            'camera = rw_sensors.ROS_camera_node:main' 
        ],
    },
)
