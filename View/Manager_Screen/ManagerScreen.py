import os

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from View.screens import screens


class ManagerScreen(ScreenManager):

    # List of screens
    _screenNames = []

    # Constructor
    def __init__(self, **kwargs):
        # Inherited Attributes
        super().__init__(**kwargs)
        # Attributes
        self.app = MDApp.get_running_app()
    
    def on_current(self, *args):
        super().on_current(*args)

    def load_common_package(self, name_screen) -> None:
        def _load_kv(path_to_kv):
            kv_loaded = False
            for loaded_path_kv in Builder.files:
                if path_to_kv in loaded_path_kv:
                    kv_loaded = True
                    break
            if not kv_loaded:
                Builder.load_file(path_to_kv)
    
    def switch_screen(self, screen_name: str) -> None:
        def switch_screen(*args):
            self.current = screen_name
            
    def add_screen(self, view) -> None:
        self.add_widget(view)