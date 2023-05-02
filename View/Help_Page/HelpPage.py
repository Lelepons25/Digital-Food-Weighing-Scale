from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_file('View\Help_Page\HelpPage.kv')

class HelpPage(Screen):
    def __init__(self, manager = None, **kwargs):
        super().__init__(**kwargs)
        self.manager = manager