import kivy
from kivy.config import Config
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

kivy.require('1.10.1') # replace with your current kivy version !
from kivy.app import App

Config.set('kivy', 'default_font', [
    'msgothic',
    'fonts/zhengti.TTF'])



Builder.load_string('''
<OneScreen>
    GridLayout:
        
        cols: 1
        rows: 2
        Button:
            text: "测试按钮"
            id: "showInfo"
            font_name: "fonts/zhengti.ttf"
            size_hint: (1, 0.9)
        BoxLayout:
            canvas.before:
                Color:
                    rgba:0, 1, 0, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: (1, 0.1)
            orientation: 'horizontal'
            Spinner:
                text: app.work1
                font_name: "fonts/zhengti.ttf"
                font_size: 20
                values: app.work1_values
                size_hint: (1, 1)
            Spinner:
                text: app.work2
                font_name: "fonts/zhengti.ttf"
                font_size: 20
                values: app.work2_values
                size_hint: (1, 1)
''')

class OneScreen(Screen):
    pass


class inStore(App):
    # def __init__(self, **kwargs):
    #     self.work1 = '存入信息'
    #     self.work2 = '查账'
    #def __init__(self):
    work1 = '录入'
    work1_values = ["录入", "查询"]
    work2 = '查账'
    work2_values = ["查账"]

    def build(self):
        return OneScreen()

if __name__ in ('__android__', '__main__'):
    inStore().run()