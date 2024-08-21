from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


# Set window size
Window.size = (500, 500)

class MyCardLayout(MDBoxLayout):
    text = StringProperty()

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.accent_palette = "Red"
        return Builder.load_file('scroll_box.kv')
    
    def on_label_press(self):
        print("pressed!!")
        
    def add_card(self):
        # Create a new MyCardLayout instance
        new_card = MyCardLayout(text = "New Card")
        
        # Add the new card to the 'word_card_area' layout
        self.root.ids.word_card_area.add_widget(new_card)
        
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
        

if __name__ == '__main__':
    MainApp().run()
    
