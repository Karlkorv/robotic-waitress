from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import inputReader
import functions

class MyButton(Button):
    def __init__(self, AnswID, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.AnswID = AnswID

class ConversationWindow(App):
    def build(self):
 
        widget_root = BoxLayout(orientation = "vertical")
        label_op = Label(size_hint_y = 15, font_size=51)

        optionTexts = []
        for key in options:
            opt = options.get(key)
            optionTexts.append(opt.Text)
        
        optionConvIDs = []
        for key1 in options:
            opt = options.get(key1)
            optionConvIDs.append(opt.ConvID)

        print(optionConvIDs)

        grid_button = GridLayout(cols = 2, size_hint_y = 20)
        counter = 0
        for text in optionTexts:
            grid_button.add_widget(MyButton(
                                            text = text,
                                            AnswID = int(optionConvIDs[counter]),
                                            size_hint = (0.7, 0.6),
                                            bold = True,
                                            background_color = '#00FFCE'
                                            ))
            counter = counter + 1
        label_op.text = functions.getRandomintroNode(intros).Text

        def reset_buttons():
            grid_button.clear_widgets()

        def add_buttons(node):
            reset_buttons()

            counter = 0
            for text in node.AnswText:
                grid_button.add_widget(MyButton(
                                            text = text,
                                            AnswID = node.AnswID[counter],
                                            size_hint = (0.7, 0.6),
                                            bold = True,
                                            background_color = '#00FFCE'
                                            ))
                counter = counter + 1

        def add_new_text(node):
            label_op.text = node.Text

        def select_conversation_node(instance):
            currentNode = functions.get_node(nodes, instance.AnswID)
            add_buttons(currentNode)
            add_new_text(currentNode)
            button_loop()

        def quit_conversation():
            ConversationWindow().exit()


        def error_conversation():
            label_op.text = "You don't seem to be interested, see you never!"
            grid_button.clear_widgets()
            Clock.schedule_once(quit_conversation, 3)

        def bye_conversation():
            label_op.text = "Bye bye now"
            grid_button.clear_widgets()
            Clock.schedule_once(quit_conversation, 3)


        def next_conversation_node(instance):
            currentNode = functions.get_node(nodes, int(instance.AnswID)) #placeholder
            if currentNode == None:
                error_conversation()
                return
            if int(currentNode.AnswID[0])/1000 == 9:
                bye_conversation()
                return

            add_buttons(currentNode)
            add_new_text(currentNode)
            button_loop()

        for button in grid_button.children:
                print("in options buttonLoop")
                button.bind(on_press = select_conversation_node)

        def button_loop():
            for button in grid_button.children:
                button.bind(on_press = next_conversation_node)

        def label_text_size(label, new_height):
            label.fontsize = 0.5*label.height
        label_op.bind(height = label_text_size)

        widget_root.add_widget(label_op)
        widget_root.add_widget(grid_button)

        return widget_root


intros = inputReader.readInputIntros('input.txt')
options = inputReader.readInputOptions('input.txt')
nodes = inputReader.readInputNodes('input.txt')


numOfOptions = len(options)
selected = False

    
ConversationWindow().run()