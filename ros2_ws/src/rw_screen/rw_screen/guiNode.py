from rw_screen import functions
from rw_screen import inputReader
from rw_screen import classes
from rw_interfaces.msg import RobotStatus, DisplayStatus
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
import time
from multiprocessing import Process, Pipe
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import os
from std_msgs.msg import Header
#sys.path.append('/home/ubuntu/ros2_ws/src/stevan_screen/stevan_screen/')

path = os.getcwd()
path = path + '/src/rw_screen/rw_screen/'

options = inputReader.readInputOptions(path)
intros = inputReader.readInputIntros(path)
nodes = inputReader.readInputNodes(path)
farewells = inputReader.readInputFarewells(path)
starts = inputReader.readInputConvStarts(path)

class VideoWindow(App):
    """
    A Kivy application to display a video file on a window.
    Attributes:
        pipe (multiprocessing.Pipe): A pipe used for communication between processes.
    Methods:
        build(): Overrides the build() method of the parent class to create a window
            and display the video.
        update_video_source(dt): Updates the video source of the window.
    """

    def __init__(self, pipe):
        """
        Constructs a VideoWindow object.
        Args:
            pipe (multiprocessing.Pipe): A pipe used for communication between processes.
        """
        self.pipe = pipe
        super().__init__()

    def build(self):
        """
        Overrides the build() method of the parent class to create a window and display the video.
        Returns:
            Video: A Kivy Video widget displaying a video.
        """
        self.currAnimation = path + 'animations/roaming_eye_loop.mp4'
        self.video = Video(source=self.currAnimation)
        self.video.loaded = True
        self.video.allow_stretch = True
        self.video.volume = 0
        self.video.state = 'play'
        self.video.options = {'eos': 'loop'}
        Clock.schedule_interval(self.update_video_source, 0.1)  # Schedule the update function to run every 0.1 seconds
        return self.video

    def update_video_source(self, dt):
        """
        Updates the video source of the window.
        Args:
            dt (float): The delta time since the last call.
        """
        if self.pipe.poll():
            nextAnimation = self.pipe.recv()
            if nextAnimation is not None and nextAnimation != self.currAnimation:
                print(nextAnimation)
                self.video.source = nextAnimation
                self.currAnimation = nextAnimation
                nextAnimation = None

class MyButton(Button):
    """
    A subclass of Kivy Button with an additional attribute for the button's answer ID.
    Attributes:
        ButtonAnswID (int): The ID of the answer associated with the button.
    Methods:
        __init__(ButtonAnswID, **kwargs): Initializes a MyButton object.
    """

    def __init__(self, ButtonAnswID, **kwargs):
        """
        Initializes a MyButton object.
        Args:
            ButtonAnswID (int): The ID of the answer associated with the button.
            **kwargs: Additional keyword arguments.
        """
        super(MyButton, self).__init__(**kwargs)
        self.ButtonAnswID = ButtonAnswID
        self.markup = True
        self.font_name = "Avenir_LT_pro_heavy"
        self.font_size = 40

                    
class MyLabel(Label):
    """
    A subclass of Kivy Label.
    Attributes:
        text (str): The current text of the label.
        target_text (str): The target text of the label.
        index (int): The current index in the target text.
    Methods:
        __init__(**kwargs): Initializes a MyLabel object.
        change_text(text): Changes the text of the label.
        update_text(dt): Updates the text of the label.
    """
    def __init__(self, **kwargs):
        """
        Initializes a MyLabel object.
        Args:
            **kwargs: Additional keyword arguments.
        """
        super().__init__(**kwargs)
        self.text = ''
        self.target_text = 'Hello, world!'
        self.index = 0

    def change_text(self, text):
        """
        Changes the text of the label.
        Args:
            text (str): The new text to display.
        """
        self.text = ''
        self.target_text = text
        Clock.schedule_interval(self.update_text, 0.05)


    def update_text(self, dt):
        """
        Updates the text of the label.
        Args:
            dt (float): The delta time since the last call.
        """
        if self.index >= len(self.target_text):
            Clock.unschedule(self.update_text)
            self.index = 0
            return
        self.text += self.target_text[self.index]
        self.index += 1

class ConversationWindow(App):
    """
    ConversationWindow class - the GUI window application.
    Attributes:
        pipe (multiprocessing.Pipe): A pipe used for communication between processes.
        vid_pipe (multiprocessing.Pipe): A pipe used for communication between processes.
        activeConv (bool): A flag indicating whether a conversation is currently active.
        currAnimation (str): The current animation being displayed.
    Methods:
        __init__(pipe, vid_pipe): Initializes a ConversationWindow object.
        build(): Overrides the build() method of the parent class to create a window and display the GUI.
        checkPipe(dt): Checks for incoming messages on the pipe.
        startConversation(): Starts a new conversation.
        sendMessage(btn): Sends a message to the robot.
        updateGUI(gui_msg): Updates the GUI based on the received message.
        farewell(): Says goodbye to the user and ends the conversation.
    """
    def __init__(self, pipe, vid_pipe):
        """
        Initializes a ConversationWindow object.
        Args:
            pipe (multiprocessing.Pipe): A pipe used for communication between processes.
            vid_pipe (multiprocessing.Pipe): A pipe used for communication between processes.
        """
        self.pipe = pipe
        self.vid_pipe = vid_pipe
        self.activeConv = False
        self.currAnimation = path + 'roaming_eye_loop.mp4'
        print(f"{options.__str__()}")

        LabelBase.register(name='Avenir_LT_pro_heavy',
                        fn_regular= path + 'fonts/AvenirLTProHeavy.otf')

        # self.model = TTS.list_models()[15] # 15 is overflow model
        # self.tts = TTS(model_name=self.model, progress_bar=False, gpu=False)

        # for key in self.nodes.keys():
        #     node = self.nodes.get(key)
        #     path = "speech/" + str(node.ID) + ".wav"
        #     self.tts.tts_to_file(text=node.NoSplitText, file_path=path)
        super().__init__()
    
    def build(self):
        """
        Overrides the build() method of the parent class to create a window and display the GUI.
        """
        Clock.schedule_interval(self.checkPipe, 0.1)  # Schedule the update function to run every 0.1 seconds    
        widget_root = BoxLayout(orientation="vertical")
        mixer.init()
        return widget_root

    # Initial button setup on startup
    def initialize(self):
        """
        Initializes the conversation interface with a label and grid layout of buttons.
        Args:
            self: The object pointer.
        Returns:
            None.
        """
        # The screen consist of a BoxLayout containing one label (the text),
        # and one GridLayout (the buttons)
        label_op = MyLabel(size_hint_y=15, font_size=51, font_name = "Avenir_LT_pro_heavy")
        grid_button = GridLayout(cols=1, size_hint_y=20, padding = 10, spacing = 10)

        def add_buttons(node):
            """
            Adds buttons to the GridLayout.
            Args:
                node: The conversation node that contains the text and answer options.
            Returns:
                None.
            """
            #reset_buttons()
            counter = 0
            for text in node.AnswText:
                if counter == 0:
                    frame = path + "imgs/frame_green.png"
                    frame_pushed = path + "imgs/frame_pushed_green.png"
                elif counter == 1:
                    frame = path + "imgs/frame_red.png"
                    frame_pushed = path + "imgs/frame_pushed_red.png"
                else :
                    frame = path + "imgs/frame_orange.png"
                    frame_pushed = path + "imgs/frame_pushed_orange.png"
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
            """
            Clears the widgets from the grid layout.
            Args:
                None.
            Returns:
                None.
            """
            grid_button.clear_widgets()

        def next_conversation_node(instance):
            """
            Updates the conversation based on the selected button.
            Args:
                instance: The button instance that was pressed.
            Returns:
                None.
            """
            self.pipe.send("touch")
            time.sleep(0.5)
            EXIT_CODE = 9999
            NEW_CONV_CODE = 8888
            if int(instance.ButtonAnswID) == EXIT_CODE:
                currentNode = functions.getRandomFarewell(farewells)
                grid_button.clear_widgets()
                Clock.schedule_once(quit_conversation, 2)
            elif int(instance.ButtonAnswID) == NEW_CONV_CODE:
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
            """
            Updates the animation based on the current conversation node.
            Args:
                node: The current conversation node.
            Returns:
                None.
            """
            self.vid_pipe.send(node.Animation)

        def button_loop():
            """
            Binds the 'next_conversation_node' function to each button in the grid layout.
            Args:
                None.
            Returns:
                None.
            """
            for button in grid_button.children:
                button.bind(on_press=next_conversation_node)

        def add_new_text(node):
            """
            Updates the conversation label with new text and plays TTS audio.
            Args:
                node: The current conversation node.
            Returns:
                None.
            """
            label_op.change_text(node.Text)
            audiopath = path + "speech/intro_1.wav" # Temp
            if isinstance(node, classes.convNode):
                audiopath = path + "speech/" + str(node.ID) + ".wav"
            elif isinstance(node, classes.intro):
                audiopath = path + "speech/intro_" + str(node.ID) + ".wav"
            elif isinstance(node, classes.convStart):
                audiopath = path + "speech/start_" + str(node.ID) + ".wav"
            elif isinstance(node, classes.farewell):
                audiopath = path + "speech/farewell_" + str(node.ID) + ".wav"
            print(f"Audiopath: {audiopath}")
            sound = mixer.Sound(audiopath)
            sound.play()

        def label_text_size(label, new_height):
            """
            Set the font size of the label based on its new height.
            Args:
                label (MyLabel): The label widget to set the font size for.
                new_height (int): The new height of the label.
            Returns:
                None
            """
            label.fontsize = 0.5*label.height

        def quit_conversation(temp):
            """
            Ends the conversation by sending the 'convEnd' message through a pipe,
            and then sets the active conversation flag to False.
            Parameters:
                temp (Event): The event that triggered this function.
            Returns:
                None
            """
            self.vid_pipe.send(path + "animations/roaming_eye_loop.mp4")
            self.pipe.send("convEnd")
            time.sleep(2)
            self.activeConv = False

        counter = 0
        for key in options:
            opt = options.get(key)
            if counter == 0:
                frame = path + "imgs/frame_green.png"
                frame_pushed = path + "imgs/frame_pushed_green.png"
            elif counter == 1:
                frame = path + "imgs/frame_red.png"
                frame_pushed = path + "imgs/frame_pushed_red.png"
            else :
                frame = path + "imgs/frame_orange.png"
                frame_pushed = path + "imgs/frame_pushed_orange.png"
            assert opt is not None
            b = MyButton(
                text = opt.Text,
                background_down = frame_pushed,
                background_normal = frame,
                ButtonAnswID=opt.ButtonAnswID,
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
        """
        Checks for incoming messages on the pipe.
        Args:
            dt (float): Time interval between checks.
        """
        if self.activeConv == True:
            if self.pipe.poll(): 
                if self.pipe.recv() == False:
                    self.root.clear_widgets()
                    self.pipe.send("convEnd")
                    self.activeConv = False
            else:
                return
        elif self.pipe.poll():
            self.activeConv = self.pipe.recv()
            if self.activeConv == True:
                self.initialize()
        else:
            self.root.clear_widgets()
            
class guiNode(Node):
    """
    This module contains the guiNode class that is a subclass of the Node class.
    It provides a graphical user interface for the robot's interaction.
    Classes:
        guiNode
    Methods:
        startConv(pipe, vid_pipe): a static method that starts a ConversationWindow object with the given pipes.
        startVid(pipe): a static method that starts a VideoWindow object with the given pipe.
        __init__(): a constructor method that initializes the guiNode object.
        start_callback(msg: RobotStatus): a method that is called when a RobotStatus message is received. It sets the conversation status and sends a message to the ConversationWindow.
        timer_callback(): a method that is called by a timer at a set interval. It checks if a message has been received from the ConversationWindow and updates the display status accordingly.
        main(args=None): the main function that initializes the guiNode and runs the ROS2 node.
    """
    
    @staticmethod
    def startConv(pipe, vid_pipe):
        """
        A static method that starts a `ConversationWindow` object with the given pipes.
        Args:
            pipe : A pipe used for communication between the `guiNode` and `ConversationWindow`.
            vid_pipe: A pipe used for communication between the `guiNode` and `VideoWindow`.
        """
        ConversationWindow(pipe, vid_pipe).run()

    @staticmethod
    def startVid(pipe):
        """
        A static method that starts a `VideoWindow` object with the given pipe.
        Args:
            pipe: A pipe used for communication between the `guiNode` and `VideoWindow`.
        """
        VideoWindow(pipe).run()

    def __init__(self):
        """
        Constructor method that initializes the `guiNode` object.
        """
        super().__init__("guiNode") # type: ignore
        self.get_logger().info("'guiNode' started")
        self.guiPublisher = self.create_publisher(DisplayStatus, "touchscreen_feedback", 10)
        self.guiSubscriber = self.create_subscription(
            RobotStatus, "behaviour", self.start_callback, 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        self.conv_pipe, self.conv_pipe_child = Pipe()
        self.vid_pipe, self.vid_pipe_child = Pipe()
        p1 = Process(target=guiNode.startConv, args=(self.conv_pipe_child, self.vid_pipe,))
        p1.start()
        p2 = Process(target=guiNode.startVid, args=(self.vid_pipe_child,))
        p2.start()
        Clock.schedule_interval(self.timer_callback, 0.1)  # Schedule the update function to run every 0.1 seconds    
    
    def start_callback(self, msg: RobotStatus):
        """
        A method that is called when a `RobotStatus` message is received. It sets the conversation status and sends a message to the `ConversationWindow`.

        Args:
            msg: A `RobotStatus` message object.
        """
        if msg.roam == False:
            header = Header()
            header.stamp = self.get_clock().now().to_msg()
            msg2 = DisplayStatus()
            msg2.in_conversation = True
            msg2.header = header
            self.guiPublisher.publish(msg2)
            self.conv_pipe.send(True)
        if msg.roam == True:
            self.conv_pipe.send(False)
    
    def timer_callback(self):
        """
        Timer callback function that is called periodically by the ROS2 timer.
        
        This function checks the status of the conversation pipe, and publishes DisplayStatus messages to a ROS2 topic
        based on the result of the conversation pipe.
        
        If the conversation pipe returns "convEnd", the function publishes a DisplayStatus message with 'in_conversation' 
        field set to False.
        
        If the conversation pipe returns "touch", the function publishes a DisplayStatus message with 'in_conversation' 
        field set to True.
        """
        if self.conv_pipe.poll():
            pipeRes = self.conv_pipe.recv()
            print(f"pipeRes: {pipeRes}")
            header = Header()
            header.stamp = self.get_clock().now().to_msg()
            msg = DisplayStatus()
            msg.header = header
            if pipeRes == "convEnd":
                msg.in_conversation = False
            if pipeRes == "touch":
                msg.in_conversation = True
            self.guiPublisher.publish(msg)
    
def main(args=None):
    rclpy.init(args=args)
    node = guiNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
