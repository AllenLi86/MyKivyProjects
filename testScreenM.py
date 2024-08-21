from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

KV = '''
ScreenManager:
    StartScreen:
    HomeScreen:

<StartScreen>:
    name: 'start'
    MDRaisedButton:
        text: "START"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.switch_to_home()

<HomeScreen>:
    name: 'home'
    MDRaisedButton:
        text: "HOME SCREEN"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.switch_to_start()
'''

class StartScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def switch_to_home(self):
        self.root.current = 'home'

    def switch_to_start(self):
        self.root.current = 'start'

MainApp().run()
