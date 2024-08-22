from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.utils import get_color_from_hex
import uuid


# Set window size
Window.size = (400, 600)

class Content(MDBoxLayout):
    pass

class MyCardLayout(MDBoxLayout):
    text = StringProperty()

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.accent_palette = "Red"
        return Builder.load_file('scroll_box.kv')
    
    def on_wordcard_label_press(self):
        print("pressed!!")

    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()
                
    def show_addWordCard_dialog(self):
        # if not self.dialog:
        self.dialog = MDDialog(
            title="Add new word",
            type="custom",
            content_cls=Content(),
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.add_card
                ),
            ],
        )
        self.dialog.open()
        
    def add_card(self, *args):
        WMS_data = self.get_text_inputs()  # 取得用戶輸入的資料
        card_id = str(uuid.uuid4())  # 生成唯一的 ID
        
        # Create a new MyCardLayout instance
        new_card = MyCardLayout(text = WMS_data["word"])
        
        # Add the new card to the 'word_card_area' layout
        self.root.ids.word_card_area.add_widget(new_card)
        
        # 紀錄字卡資料
        self.record_card_data(card_id, WMS_data)
        
    def get_text_inputs(self, *args):
        # 取得 kv 文件中定義的 ID 並讀取相應的文字
        word = self.dialog.content_cls.ids.word_input.text
        meaning = self.dialog.content_cls.ids.meaning_input.text
        sentence = self.dialog.content_cls.ids.sentence_input.text

        print(f"Word: {word}")
        print(f"Meaning: {meaning}")
        print(f"Sentence: {sentence}")

        self.close_dialog()   
        return {
            "word": word,
            "meaning": meaning,
            "sentence": sentence
        }
        
    def record_card_data(self, card_id, data):
        # 將每張字卡的資料儲存到列表中
        if not hasattr(self, 'card_data'):
            self.card_data = {}

        self.card_data.update({card_id: 
            {"word": data["word"],
             "meaning": data["meaning"],
             "sentence": data["sentence"],
             }
            })
        print(f"Card Data Recorded: {self.card_data}")
        
    

if __name__ == '__main__':
    MainApp().run()
    
