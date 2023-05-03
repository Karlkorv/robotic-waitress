from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import BorderImage
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.properties import BooleanProperty
from kivy.uix.video import Video
from TTS.api import TTS
from pygame import mixer
import inputReader
import functions
import time
from multiprocessing import Process, Pipe


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
                """ self.video.state = 'stop'
                self.video.load()
                self.video.state = 'play' """
                currAnimation = nextAnimation
                nextAnimation = None



class MyButton(Button):
    """MyButton class - subclass of Kivy Button, with addition of AnswID,
    representing what node the button leads to"""

    def __init__(self, ButtonAnswID, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.ButtonAnswID = ButtonAnswID
        self.markup = True
        self.font_name = "Avenir_LT_pro_heavy"
        self.font_size = 40

        """  self.canvas.before: BorderImage(
                    size=(self.width, self.height),
                    pos=(self.x, self.y),
                    border=(16, 8, 16, 8),
                    source='button.png',
                    auto_scale = 'both',
                    display_border = True ) """
                    
        
class MyLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = ''
        self.target_text = 'Hello, world!'
        self.index = 0

    def change_text(self, text):
         self.text = ''
         self.target_text = text
         Clock.schedule_interval(self.update_text, 0.05)


    def update_text(self, dt):
        if self.index >= len(self.target_text):
            Clock.unschedule(self.update_text)
            self.index = 0
            return
        self.text += self.target_text[self.index]
        self.index += 1

class ConversationWindow(App):
    """ConversationWindow class - the GUI window application"""

    def __init__(self, pipe, vid_pipe):
        self.pipe = pipe
        self.vid_pipe = vid_pipe
        self.activeConv = False
        super().__init__()
    
    def build(self):
        Clock.schedule_interval(self.checkPipe, 0.1)  # Schedule the update function to run every 0.1 seconds    
        widget_root = BoxLayout(orientation="vertical")
        return widget_root

    # Initial button setup on startup
    def initialize(self):
        # The screen consist of a BoxLayout containing one label (the text),
        # and one GridLayout (the buttons)
        label_op = MyLabel(size_hint_y=15, font_size=51, font_name = "Avenir_LT_pro_heavy")
        grid_button = GridLayout(cols=1, size_hint_y=20, padding = 10, spacing = 10)

        def add_buttons(node):
            #reset_buttons()
            counter = 0
            for text in node.AnswText:
                if counter == 0:
                    frame = "imgs/frame_green.png"
                    frame_pushed = "imgs/frame_pushed_green.png"
                elif counter == 1:
                    frame = "imgs/frame_red.png"
                    frame_pushed = "imgs/frame_pushed_red.png"
                else :
                    frame = "imgs/frame_orange.png"
                    frame_pushed = "imgs/frame_pushed_orange.png"
                b = MyButton(
                    text = text,
                    background_normal = frame,
                    background_down = frame_pushed,
                    ButtonAnswID = node.AnswID[counter],
                    bold = True
                )
                grid_button.add_widget(b)
                counter = counter + 1

        def reset_buttons():
            grid_button.clear_widgets()

        def next_conversation_node(instance):
            time.sleep(0.5)
            if int(instance.ButtonAnswID) == 9999:  # Exit code
                currentNode = functions.getRandomFarewell(farewells)
                grid_button.clear_widgets()
                Clock.schedule_once(quit_conversation, 2)
            elif int(instance.ButtonAnswID) == 8888: # New conversation code
                currentNode = functions.getRandomConvStart(starts)
                reset_buttons()
                add_buttons(currentNode)
                update_animation(currentNode)
            else:
                currentNode = functions.get_node(
                    nodes, int(instance.ButtonAnswID))
                reset_buttons()
                add_buttons(currentNode)
                update_animation(currentNode)
            add_new_text(currentNode)
            button_loop()

        def update_animation(node):
            self.vid_pipe.send(node.Animation)

        def button_loop():
            for button in grid_button.children:
                button.bind(on_press=next_conversation_node)

        def add_new_text(node):
            label_op.change_text(node.Text)
            #if int(node.ID) >= 1000:
            #    path = "speech/" + str(node.ID) + ".wav"
            #    sound = mixer.Sound(path)
            #    sound.play()

        def label_text_size(label, new_height):
            label.fontsize = 0.5*label.height

        def quit_conversation(temp):
            self.vid_pipe.send("animations/roaming_eye_loop.mp4")
            time.sleep(2)
            self.activeConv = False

        counter = 0
        for key in options:
            opt = options.get(key)
            if counter == 0:
                frame = "imgs/frame_green.png"
                frame_pushed = "imgs/frame_pushed_green.png"
            elif counter == 1:
                frame = "imgs/frame_red.png"
                frame_pushed = "imgs/frame_pushed_red.png"
            else :
                frame = "imgs/frame_orange.png"
                frame_pushed = "imgs/frame_pushed_orange.png"
            b = MyButton(
                text = opt.Text,
                background_down = frame_pushed,
                background_normal = frame,
                ButtonAnswID=opt.ConvID,
                pos_hint = {'center_x': 0.5},
                bold = True,
            )
            
            grid_button.add_widget(b)
            counter = counter + 1

        for button in grid_button.children:
            button.bind(on_press=next_conversation_node)

        # Initial label setup on startup
        add_new_text(functions.getRandomintroNode(intros))
        label_op.bind(height=label_text_size)

                # Add the widgets to the BoxLayout
        self.root.add_widget(label_op)
        self.root.add_widget(grid_button)
    
        
    def checkPipe(self, dt):
        if self.pipe.poll():
            self.activeConv = self.pipe.recv()
            if self.activeConv:
                self.initialize()
        if self.activeConv == False:
            self.root.clear_widgets()


# Global variables
currAnimation = 'animations/roaming_eye_loop.mp4'
intros = inputReader.readInputIntros('input.txt')
options = inputReader.readInputOptions('input.txt')
nodes = inputReader.readInputNodes('input.txt')
farewells = inputReader.readInputFarewells('input.txt')
starts = inputReader.readInputConvStarts('input.txt')
LabelBase.register(name='Avenir_LT_pro_heavy',
                fn_regular='fonts/AvenirLTProHeavy.otf')


""" model = TTS.list_models()[15] # 15 is overflow model
tts = TTS(model_name=model, progress_bar=False, gpu=False) """

""" for key in nodes.keys():
    node = nodes.get(key)
    path = "speech/" + str(node.ID) + ".wav"
    tts.tts_to_file(text=node.NoSplitText, file_path=path) """

#tts.tts_to_file(text="This is a test", file_path="speech/test.wav")


mixer.init()

def startConv(pipe, vid_pipe):
    ConversationWindow(pipe, vid_pipe).run()

def startVid(pipe):
    VideoWindow(pipe).run()

if __name__ == '__main__':

    conv_pipe, conv_pipe_child = Pipe()
    vid_pipe, vid_pipe_child = Pipe()

    p1 = Process(target=startConv, args=(conv_pipe_child, vid_pipe, ))
    p1.start()


    p2 = Process(target=startVid, args=(vid_pipe_child,))
    p2.start()

    time.sleep(5)
    print("STARTED!")
    conv_pipe.send(True)

    """ time.sleep(10)
    print("STARTED! AGAIN!")
    conv_pipe.send(True) """

    #conv_pipe.send("Start")


