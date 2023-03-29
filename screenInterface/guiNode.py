#!/usr/bin/env python3

from stevan_screen import functions
from stevan_screen import inputReader
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


import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
sys.path.append('/home/ubuntu/ros2_ws/src/stevan_screen/stevan_screen/')

intros = inputReader.readInputIntros(
    '/home/ubuntu/ros2_ws/src/stevan_screen/stevan_screen/input.txt')
options = inputReader.readInputOptions(
    '/home/ubuntu/ros2_ws/src/stevan_screen/stevan_screen/input.txt')
nodes = inputReader.readInputNodes(
    '/home/ubuntu/ros2_ws/src/stevan_screen/stevan_screen/input.txt')
farewells = inputReader.readInputFarewells(
    '/home/ubuntu/ros2_ws/src/stevan_screen/stevan_screen/input.txt')

model = TTS.list_models()[15] # 15 is overflow model
tts = TTS(model_name=model, progress_bar=False, gpu=False) 

for key in nodes.keys():
    node = nodes.get(key)
    path = "speech/" + str(node.ID) + ".wav"
    tts.tts_to_file(text=node.NoSplitText, file_path=path) 



class MyButton(Button):
    """MyButton class - subclass of Kivy Button, with addition of AnswID,
    representing what node the button leads to"""

    def __init__(self, ButtonAnswID, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.ButtonAnswID = ButtonAnswID


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
                b = MyButton(
                    text=text,
                    ButtonAnswID=node.AnswID[counter],
                    size_hint=(0.7, 0.6),
                    bold=True
                )
                grid_button.add_widget(b)

                counter = counter + 1

        def add_new_text(node):
            """Adds text to the top of the screen"""
            label_op.text = node.Text

        def quit_conversation(temp):
            ConversationWindow().stop()

        def next_conversation_node(instance):
            """Updates the screen when button 'instance' is clicked"""
            if int(instance.ButtonAnswID) == 9999:  # Exit code
                currentNode = functions.getRandomFarewell(farewells)
                grid_button.clear_widgets()
                Clock.schedule_once(quit_conversation, 1)
                # TODO : Restart application as robot walks away
            else:
                currentNode = functions.get_node(
                    nodes, int(instance.ButtonAnswID))
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
        label_op = Label(size_hint_y=15, font_size=51)

        # Initial button setup on startup
        grid_button = GridLayout(cols=2, size_hint_y=20)
        for key in options:
            opt = options.get(key)
            b = MyButton(
                text=opt.Text,
                ButtonAnswID=opt.ConvID,
                size_hint=(0.7, 0.6),
                bold=True
            )
            grid_button.add_widget(b)

        for button in grid_button.children:
            button.bind(on_press=next_conversation_node)

        # Initial label setup on startup
        label_op.text = functions.getRandomintroNode(intros).Text
        label_op.bind(height=label_text_size)

        # Add the widgets to the BoxLayout
        widget_root.add_widget(label_op)
        widget_root.add_widget(grid_button)

        return widget_root


class MyNode(Node):

    def __init__(self):
        super().__init__("start_conv_subscriber")
        self.get_logger().info("'start_conv_node' started")
        self.sub_ = self.create_subscription(
            String, "/chatter", self.start_callback, 10)

    def start_callback(self, msg: String):
        self.get_logger().info(str(msg))
        ConversationWindow().run()


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
