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



class Gauge(Widget):

    unit = NumericProperty(1.8)
    value = BoundedNumericProperty(0, min=0, max=100, errorvalue=0)
    path = dirname(abspath(__file__))
    file_gauge = StringProperty(join(path, "cadran.png"))
    file_needle = StringProperty(join(path, "needle.png"))
    size_gauge = BoundedNumericProperty(128, min=128, max=256, errorvalue=128)
    size_text = NumericProperty(10)

    def __init__(self, **kwargs):
        super(Gauge, self).__init__(**kwargs)

        self._gauge = Scatter(
            size=(1350,600),
            do_rotation=False,
            do_scale=False,
            do_translation=False
        )

        _img_gauge = Image(
            source=self.file_gauge,
            size=(1350,600)

        )

        self._needle = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False
        )

        _img_needle = Image(
            source=self.file_needle,
            size=(self.size_gauge, self.size_gauge)
        )

        self._glab = Label(font_size=self.size_text, markup=True)
        self._progress = ProgressBar(max=100, height=20, value=self.value , size=(500,400))

        self._gauge.add_widget(_img_gauge)
        self._needle.add_widget(_img_needle)

        self.add_widget(self._gauge)
        self.add_widget(self._needle)
        self.add_widget(self._glab)
        self.add_widget(self._progress)

        self.bind(pos=self._update)
        self.bind(size=self._update)
        self.bind(value=self._turn)

    def _update(self, *args):
        '''
        Update gauge and needle positions after sizing or positioning.
        '''
        self._gauge.pos = self.pos
        self._needle.pos = (self.x, self.y)
        self._needle.center = self._gauge.center
        self._glab.center_x = self._gauge.center_x
        self._glab.center_y = self._gauge.center_y + (self.size_gauge / 4)
        self._progress.x = self._gauge.x + (self.size_gauge/0.468 )
        self._progress.y = self._gauge.y + (self.size_gauge/4 )
        self._progress.width = self.size_gauge

    def _turn(self, *args):
        '''
        Turn needle, 1 degree = 1 unit, 0 degree point start on 50 value.
        '''
        self._needle.center_x = self._gauge.center_x
        self._needle.center_y = self._gauge.center_y
        self._needle.rotation = (50 * self.unit) - (self.value * self.unit)
        self._glab.text = "[b]{0:.0f}[/b]".format(self.value)
        self._progress.value = self.value


class StartScreen(Screen):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.do_something(), 1 / 60)


    def do_something(self):
        self.manager.current = "Main"


class MainScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.gauge = Gauge(value=50, size_gauge=256, size_text=50, pos_hint={"center_x": 0.18, "center_y": 0.1})
        self.add_widget(self.gauge)


    def set_current_velocity(self, velocity):
        self.gauge.value = velocity


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
