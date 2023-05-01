from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('View\More_Page\MorePage.kv')

# More Page displays the other categories
class MorePage(Screen):
    print("here")
    pass