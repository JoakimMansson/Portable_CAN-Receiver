import os

from kivy.clock import Clock
from kivy.properties import ObjectProperty, NumericProperty, BoundedNumericProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu

from kivy.config import Config

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import BoundedNumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from os.path import join, dirname, abspath
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window




class MainScreen(Screen):
    neutralB = ObjectProperty(None)
    reverseB = ObjectProperty(None)
    driveB = ObjectProperty(None)
    current_speed = ObjectProperty(None)

    bms_temp_img = ObjectProperty(None)
    motor_temp_img = ObjectProperty(None)


    def __init__(self, **kw):
        super().__init__(**kw)



    def set_current_velocity(self, velocity):
        self.current_speed.text = str(velocity)


    def reverse(self):
        self.reverseB.line_color = (0/255, 109/255, 176/255, 1)
        self.reverseB.text_color = (0/255, 109/255, 176/255, 1)

        self.driveB.line_color = (1, 1, 1, 1)
        self.driveB.text_color = (1, 1, 1, 1)

        self.neutralB.line_color = (1, 1, 1, 1)
        self.neutralB.text_color = (1, 1, 1, 1)


    def drive(self):
        self.driveB.line_color = (0 / 255, 109 / 255, 176 / 255, 1)
        self.driveB.text_color = (0 / 255, 109 / 255, 176 / 255, 1)

        self.reverseB.line_color = (1, 1, 1, 1)
        self.reverseB.text_color = (1, 1, 1, 1)

        self.neutralB.line_color = (1, 1, 1, 1)
        self.neutralB.text_color = (1, 1, 1, 1)


    def neutral(self):
        self.neutralB.line_color = (0 / 255, 109 / 255, 176 / 255, 1)
        self.neutralB.text_color = (0 / 255, 109 / 255, 176 / 255, 1)

        self.reverseB.line_color = (1, 1, 1, 1)
        self.reverseB.text_color = (1, 1, 1, 1)

        self.driveB.line_color = (1, 1, 1, 1)
        self.driveB.text_color = (1, 1, 1, 1)



class WindowManager(ScreenManager):
    enter_name_screen = ObjectProperty(None)
    connect_screen = ObjectProperty(None)
    home_screen = ObjectProperty(None)


class AlarmApp(MDApp):

    def build(self):
        kv = Builder.load_file(os.path.realpath("my.kv"))
        Window.size = (800, 480)
        return kv





if __name__ == "__main__":
    AlarmApp().run()
