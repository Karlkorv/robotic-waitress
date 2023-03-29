from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import BorderImage
from kivy.clock import Clock
from kivy.core.text import LabelBase
from TTS.api import TTS
from pygame import mixer
import os
import inputReader
import functions
import time


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

    def build(self):

        def reset_buttons():
            """Removes all buttons"""
            grid_button.clear_widgets()

        def add_buttons(node):
            """Adds all buttons from the current node"""
            reset_buttons()
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

        def add_new_text(node):
            """Adds text to the top of the screen"""
            label_op.change_text(node.Text)
            if int(node.ID) >= 1000:
                path = "speech/" + str(node.ID) + ".wav"
                sound = mixer.Sound(path)
                sound.play()


        def quit_conversation(temp):
            ConversationWindow().stop()

        def next_conversation_node(instance):
            time.sleep(0.5)
            """Updates the screen when button 'instance' is clicked"""
            if int(instance.ButtonAnswID) == 9999:  # Exit code
                currentNode = functions.getRandomFarewell(farewells)
                grid_button.clear_widgets()
                Clock.schedule_once(quit_conversation, 2)
                # TODO : Restart application as robot walks away
            else:
                currentNode = functions.get_node(
                    nodes, int(instance.ButtonAnswID))
                reset_buttons()
                add_buttons(currentNode)
            add_new_text(currentNode)
            button_loop()

        def button_loop():
            """Continously binds buttons to call next_conversation_node on click"""
            for button in grid_button.children:
                button.bind(on_press=next_conversation_node)

        def label_text_size(label, new_height):
            label.fontsize = 0.5*label.height

        # The screen consist of a BoxLayout containing one label (the text),
        # and one GridLayout (the buttons)
        widget_root = BoxLayout(orientation="vertical")
        label_op = MyLabel(size_hint_y=15, font_size=51, font_name = "Avenir_LT_pro_heavy")


        # Initial button setup on startup
        grid_button = GridLayout(cols=1, size_hint_y=20, padding = 10, spacing = 10)
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
        widget_root.add_widget(label_op)
        widget_root.add_widget(grid_button)

        return widget_root


intros = inputReader.readInputIntros('input.txt')
options = inputReader.readInputOptions('input.txt')
nodes = inputReader.readInputNodes('input.txt')
farewells = inputReader.readInputFarewells('input.txt')
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

ConversationWindow().run()


