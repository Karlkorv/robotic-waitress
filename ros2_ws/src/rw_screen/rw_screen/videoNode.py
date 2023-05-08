#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.video import Video

# Global variables
nextAnimation = None
currAnimation = 'animations/roaming_eye_loop.mp4'

class VideoWindow(App):
    def build(self):
        self.video = Video(source=currAnimation, preview='eye_preview.png')
        self.video.loaded = True
        self.video.allow_stretch = True
        self.video.volume = 0
        self.video.state = 'play'
        self.video.options = {'eos': 'loop'}
        Clock.schedule_interval(self.update_video_source, 0.1)  # Schedule the update function to run every 0.1 seconds
        return self.video

    def update_video_source(self, dt):
        global nextAnimation, currAnimation
        if nextAnimation is not None and nextAnimation != currAnimation:
            self.video.source = nextAnimation
            """             self.video.state = 'stop'
            self.video.load()
            self.video.state = 'play' """
            currAnimation = nextAnimation
            nextAnimation = None
    
    def to_std(place):
        global nextAnimation
        nextAnimation = 'animations/std_conv_loop.mp4'

    def to_supr(place):
        global nextAnimation
        nextAnimation = 'animations/suprised.mp4'







class VideoNode(Node):
    def __init__(self):
        super().__init__("video_screen_node")
        self.get_logger().info("'video_screen_node' started")
        self.sub_ = self.create_subscription(
            animation, "/ScreenStatus", self.start_callback, 10)
        VideoWindow().run()

    def start_callback(self, msg: animation):
        global nextAnimation
        nextAnimation = str(msg) #Kan va fel, beror på.

def main(args=None):
    rclpy.init(args=args)
    node = VideoNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()