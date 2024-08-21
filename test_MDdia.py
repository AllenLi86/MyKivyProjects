from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

KV = '''
Screen:
    MDRaisedButton:
        text: "SHOW DIALOG"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.show_dialog()
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_dialog(self):
        self.dialog = MDDialog(
            title="This is a title",
            text="This is some text",
            buttons=[
                MDFlatButton(
                    text="CANCEL", on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="OK", on_release=self.close_dialog
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

MainApp().run()
