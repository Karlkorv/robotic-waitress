from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import BorderImage
from kivy.clock import Clock
import inputReader
import functions


class MyButton(Button):
    """MyButton class - subclass of Kivy Button, with addition of AnswID,
    representing what node the button leads to"""

    def __init__(self, ButtonAnswID, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.ButtonAnswID = ButtonAnswID
        self.background_down
        self.markup = True
        self.font_size = 40

        """  self.canvas.before: BorderImage(
                    size=(self.width, self.height),
                    pos=(self.x, self.y),
                    border=(16, 8, 16, 8),
                    source='button.png',
                    auto_scale = 'both',
                    display_border = True ) """
                    
        


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
                    frame = "frame_green.png"
                elif counter == 1:
                    frame = "frame_red.png"
                else :
                    frame = "frame_orange.png"
                b = MyButton(
                    text = text,
                    background_normal = frame,
                    ButtonAnswID = node.AnswID[counter],
                    bold = True
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
                Clock.schedule_once(quit_conversation, 2)
                # TODO : Restart application as robot walks away
            else:
                currentNode = functions.get_node(
                    nodes, int(instance.ButtonAnswID))
                #Show button that was pressed
                reset_buttons()
                b = MyButton(
                    text = instance.text,
                    ButtonAnswID = instance.ButtonAnswID,
                    bold = True,
                    #background_color = '#000FFF'
                )
                grid_button.add_widget(b)
                # Delay the addition of new buttons
                Clock.schedule_once(lambda dt: add_buttons(currentNode), 1)

            Clock.schedule_once(lambda dt: add_new_text(currentNode), 1)
            Clock.schedule_once(lambda dt: button_loop(), 1)

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
        grid_button = GridLayout(cols=1, size_hint_y=20, padding = 10, spacing = 10)
        counter = 0
        for key in options:
            opt = options.get(key)
            if counter == 0:
                frame = "frame_green.png"
            elif counter == 1:
                frame = "frame_red.png"
            else :
                frame = "frame_orange.png"
            b = MyButton(
                text = opt.Text,
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
        label_op.text = functions.getRandomintroNode(intros).Text
        label_op.bind(height=label_text_size)

        # Add the widgets to the BoxLayout
        widget_root.add_widget(label_op)
        widget_root.add_widget(grid_button)

        return widget_root


intros = inputReader.readInputIntros('input.txt')
options = inputReader.readInputOptions('input.txt')
nodes = inputReader.readInputNodes('input.txt')
farewells = inputReader.readInputFarewells('input.txt')

ConversationWindow().run()


