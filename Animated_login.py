from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
from Anims import Ani

Window.size=(400,750)


class Animated(MDApp):

    def change_screen(self,name):
        screen_manager.current=name

    def build(self):
        global screen_manager
        screen_manager=ScreenManager()
        screen_manager.add_widget(Builder.load_string(Ani))
        return screen_manager

    def animated(self,widget):
        animat=Animation(pos_hint={"center_y":1.16})
        animat.start(widget)

    
    def animated1(self,widget):
        animat=Animation(pos_hint={"center_y":.86})
        animat.start(widget)

    def icons(self,widget):
        anim=Animation(pos_hint={"center_y":.8})
        anim+=Animation(pos_hint={"center_y":.85})
        anim.start(widget)

    def text(self,widget):
        anim=Animation(opacity=0,duration=2)
        anim+=Animation(opacity=1)
        anim.start(widget)


Animated().run()