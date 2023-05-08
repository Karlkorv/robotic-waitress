import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.video import Video
from multiprocessing import Process, Pipe
import time

# Global variables
currAnimation = 'animations/roaming_eye_loop.mp4'

class VideoWindow(App):

    def __init__(self, pipe):
        self.pipe = pipe
        super().__init__()

    def build(self):
        self.video = Video(source=currAnimation, preview = 'animations/robot_eye.png')
        self.video.loaded = True
        self.video.allow_stretch = True
        self.video.volume = 0
        self.video.state = 'play'
        self.video.options = {'eos': 'loop'}
        Clock.schedule_interval(self.update_video_source, 0.1)  # Schedule the update function to run every 0.1 seconds
        return self.video

    def update_video_source(self, dt):
        global currAnimation
        if self.pipe.poll():
            nextAnimation = self.pipe.recv()
            if nextAnimation is not None and nextAnimation != currAnimation:
                self.video.source = nextAnimation
                """             self.video.state = 'stop'
                self.video.load()
                self.video.state = 'play' """
                currAnimation = nextAnimation
                nextAnimation = None
            
    """ 
    def update_video_source(self, dt):
        global nextAnimation, currAnimation
        if nextAnimation is not None and nextAnimation != currAnimation:
            self.video.source = nextAnimation
            currAnimation = nextAnimation
            nextAnimation = None """
    
    def to_std(place):
        global nextAnimation
        nextAnimation = 'animations/std_conv_loop.mp4'

    def to_supr(place):
        global nextAnimation
        nextAnimation = 'animations/suprised.mp4'
    #Clock.schedule_once(to_supr, 3)




def testFunc(pipe):
        time.sleep(5)
        print("Switch")
        pipe.send('animations/suprised.mp4')
        time.sleep(5)
        print("Switch")
        pipe.send('animations/roaming_eye_loop.mp4')
        time.sleep(5)
        print("Switch")
        pipe.send('animations/suprised.mp4')
        time.sleep(5)
        print("Switch")
        pipe.send('animations/roaming_eye_loop.mp4')
        time.sleep(5)
        print("Switch")
        pipe.send('animations/suprised.mp4')
        time.sleep(5)
        print("Switch")
        pipe.send('animations/roaming_eye_loop.mp4')



def startVid(pipe):
    VideoWindow(pipe).run()

if __name__ == '__main__':

    conv_pipe, conv_pipe_child = Pipe()
    vid_pipe, vid_pipe_child = Pipe()

    p1 = Process(target=testFunc, args=(vid_pipe,))
    p1.start()


    p2 = Process(target=startVid, args=(vid_pipe_child,))
    p2.start()
    print("STARTED!")
    #conv_pipe.send("Start")




