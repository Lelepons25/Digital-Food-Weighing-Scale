from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file('View\Home_page\Homepage.kv')

class Homepage(Screen):
    # Icons for each category

    def __init__(self, **kwargs):
        super().__init__(**kwargs)




