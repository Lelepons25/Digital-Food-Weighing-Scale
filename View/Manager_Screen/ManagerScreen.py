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

    def load_common_package(self, name_screen) -> None:
        def _load_kv(path_to_kv):
            kv_loaded = False
            for loaded_path_kv in Builder.files:
                if path_to_kv in loaded_path_kv:
                    kv_loaded = True
                    break
            if not kv_loaded:
                if name_screen in ["list"]:
                    from kivy.factory import Factory
