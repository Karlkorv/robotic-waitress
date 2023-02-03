from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import inputReader
import random

class ConversationWindow(App):
    def build(self):
        widget_root = BoxLayout(orientation = "vertical")
        label_op = Label(size_hint_y = 15, font_size=51)
        symbolButton = ('1', '2', '3', '4')
        grid_button = GridLayout(cols = 2, size_hint_y = 20)
        for symbol in symbolButton :
            grid_button.add_widget(Button(
                                            text=symbol, 
                                            size_hint=(0.7, 0.6),
                                            bold= True,
                                            background_color ='#00FFCE'
                                            ))



        label_op.text = "Howdy, how you doin'?"
        

        ##for button in grid_button.children:
        ##    button.bind(on_press = text_print_button)

        def label_text_size(label, new_height):
            label.fontsize = 0.5*label.height
        label_op.bind(height = label_text_size)

        widget_root.add_widget(label_op)
        widget_root.add_widget(grid_button)

        return widget_root




ConversationWindow().run()


        