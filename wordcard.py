from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Designate .kv design file
Builder.load_file('wordcard.kv')

# Set window size
Window.size = (400, 600)

class MyLayout(Widget):
    pass

class AZWordCardApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AZWordCardApp().run()
