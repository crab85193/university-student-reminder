from ctypes.wintypes import SMALL_RECT
import datetime
import calendar
from modulefinder import Module
from select import select
from tokenize import String

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.properties import ObjectProperty, BooleanProperty


####日本語対応用コード
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分
resource_add_path('/System/Library/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')  # 追加分
####日本語対応ここまで

#ウィンドウサイズの定義
Config.set('graphics', 'width', 1200)
Config.set('graphics', 'height', 800)
Config.set('graphics', 'resizable', 0)

    
    

#popupクラス達
sm=ScreenManager()
class PopupMenu1(BoxLayout):
    popup_close = ObjectProperty(None)

class PopupMenu2(BoxLayout):
    popup_close = ObjectProperty(None)
    
class PopupMenu3(BoxLayout):
    popup_close = ObjectProperty(None)


class PopupTest(Screen):
    def popup_open(self):
        content = PopupMenu1(popup_close=self.popup_close)
        self.popup = Popup(title='課題追加', content=content, size_hint=(0.5, 0.5), auto_dismiss=True)
        self.popup.open()

class PopupTest(Screen):
    def popup_open(self):
        content = PopupMenu2(popup_close=self.popup_close)
        self.popup = Popup(title='履修講義追加', content=content, size_hint=(0.5, 0.5), auto_dismiss=True)
        self.popup.open()

class PopupTest(Screen):
    def popup_open(self):
        content = PopupMenu3(popup_close=self.popup_close)
        self.popup = Popup(title='履修講義名', content=content, size_hint=(0.5, 0.5), auto_dismiss=True)
        self.popup.open()
        
    


class PopupApp(App):
    def build(self):
        sm.add_widget(PopupTest(name=''))
        return PopupTest()
#
# Name: Menu
# Description: メニュークラス
#
class Menu(BoxLayout):
    pass

#
# Name: AttendanceScreen
# Description: 出席管理画面クラス
#
class AttendanceScreen(Screen):
    def __init__(self, **kwargs):
        super(AttendanceScreen, self).__init__(**kwargs)

#
# Name: TaskManagementScreen
# Description: 課題管理画面クラス
#
class TaskManagementScreen(Screen):
    def popup_open(self):
        content = PopupMenu1(popup_close=self.popup_close)
        self.popup = Popup(title='課題追加', content=content, size_hint=(0.7, 0.7), auto_dismiss=False)
        self.popup.open()

    def popup_close(self):
        self.popup.dismiss()
    
    label_text = ObjectProperty(None)
    check = BooleanProperty(False)

    def checkbox_check(self, checkbox):
        self.check = checkbox.active
        return

    def label_text_change(self):
        if self.check == True:
            self.label_text.text = 'CheckBox is True'
        else:
            self.label_text.text = 'CheckBox is False'
    
class TestCheckBox(App):
    def build(self):
        root = TaskManagementScreen()
        return root

#
# Name: TaskViewScreen
# Description: 課題表示クラス
#
class TaskViewScreen(Screen):
    def calender(self,year,month):
        print(type(calendar.month(year, month)))

#
# Name: LectureManagerScreen
# Description: 講義管理画面クラス
#
class LectureManagerScreen(Screen):
    def popup_open(self):
        content = PopupMenu2(popup_close=self.popup_close)
        self.popup = Popup(title='履修講義追加', content=content, size_hint=(0.7, 0.7), auto_dismiss=False)
        self.popup.open()

    def popup_close(self):
        self.popup.dismiss()

#
# Name: AssessmentScreen
# Description: 見込み評価画面クラス
#
class AssessmentScreen(Screen):
    def popup_open(self):
        content = PopupMenu3(popup_close=self.popup_close)
        self.popup = Popup(title='履修講義名', content=content, size_hint=(0.5, 0.5), auto_dismiss=True)
        self.popup.open()

    def popup_close(self):
        self.popup.dismiss()

#
# Name: View
# Description: メインメソッド
#
class View(App):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.title='StudentReminder'


    def build(self):
        # Create the screen manager

        # SM.add_widget(AttendanceScreen(name='attendance'))
        # return SM
        return Menu()

if __name__ == '__main__':
    View().run()