from kivy.app import App
from kivy.uix.video import Video


""" def on_position_change(instance, value):
    print('The position in the video is', value)

def on_duration_change(instance, value):
    print('The duration of the video is', value)

video = Video(source='robot_eye_loop.avi')
video.bind(
    position=on_position_change,
    duration=on_duration_change
) """


class VideoWindow(App):
    def Build(self):
        video = Video(source = 'robot_eye_loop.avi')
        video.loaded = True
        video.options = {'eos':'loop'}
        video.allow_stretch = True
        video.volume = 0
        video.state = "play"

        return video



if __name__ == "__main__":
    eyeVideo = VideoWindow()
    eyeVideo.run()



