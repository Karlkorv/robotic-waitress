from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import inputReader
import functions


class ConversationWindow(App):
    def build(self):
        ## Globalish
        inOptions = 1
 
        widget_root = BoxLayout(orientation = "vertical")
        label_op = Label(size_hint_y = 15, font_size=51)

        optionTexts = []
        for key in options:
            opt = options.get(key)
            optionTexts.append(opt.Text)

        grid_button = GridLayout(cols = 2, size_hint_y = 20)
        for text in optionTexts :
            grid_button.add_widget(Button(
                                            text = text,
                                            size_hint = (0.7, 0.6),
                                            bold = True,
                                            background_color = '#00FFCE'
                                            ))
        label_op.text = functions.getRandomintroNode(intros).Text

        def reset_buttons():
            grid_button.clear_widgets()

        def add_buttons(node):
            reset_buttons()
            for text in node.AnswText:
                grid_button.add_widget(Button(
                                            text = text,
                                            size_hint = (0.7, 0.6),
                                            bold = True,
                                            background_color = '#00FFCE'
                                            ))

        def add_new_text(node):
            label_op.text = node.Text

        def select_conversation_node(instance):
            currentNode = "placeholder" #placeholder
            for key in options.keys():
                option = options.get(key)
                if instance.text == option.Text:
                    currentNode = functions.getNode(nodes, int(option.ConvID))
                    break
            add_buttons(currentNode)
            add_new_text(currentNode)
            inOptions = 2

        def quit_conversation():
            label_op.text = "Bye Bye"
            grid_button.clear_widgets

        def next_conversation_node(instance):
            currentNode = "placeholder" #placeholder
            print("hoppla")
            for key in nodes.keys():
                node = nodes.get(key)
                if instance.text == node.AnswText:
                    currentNode = functions.getNode(nodes, node.AnswID)
                    break
            if currentNode == None:
                quit_conversation()
                return
            add_buttons(currentNode)
            add_new_text(currentNode)
        


        for button in grid_button.children:
            if inOptions == 1:
                button.bind(on_press = select_conversation_node)
            else:
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