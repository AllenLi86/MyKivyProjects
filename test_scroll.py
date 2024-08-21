from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

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
        

if __name__ == '__main__':
    MainApp().run()
    
    
    
    
# 問題一:kivyMD 有類似 popup的東西嗎? 有的話 請簡介

# 問題二:我想要我的app有 案某個button 畫面會更改的效果 例如 我點個start 畫面整個layout會改變>>進入 home screen之類的，這樣的話 最好的做法是使用 popup嗎? 還是有其他做法?

# 是否需要兩種layout 一種是 home screen 的 另一個是 start screen 的 透過某個button或是事件 進行切換?
