from kivy.config import Config
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', '0')
# fix the width of the window   
Config.set('graphics', 'width', '800')
# fix the height of the window
Config.set('graphics', 'height', '420')


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivy.properties import ObjectProperty, DictProperty
from database import DataBase # for Login (Test Only)
from kivy.uix.popup import Popup
from kivy.uix.label import Label


# Define the different screen
class CategoryPage(Screen):
    # Edit: Di mudisplay ang list
    def foodList(self):
        for i in range(20):
            self.name += 1
            item = TwoLineListItem(text = str(i) + ' item',
                                    secondary_text = '2nd ' + str(i) + 'th item')
            self.root.ids.food.add_widget(item)
    pass

class MorePage(Screen):
    pass

class Homepage(Screen):
    # Icons for each category
    def buttonIcons(self):
        self.ids.fruits_icon.source = 'icons/fruits.png'
        self.ids.veg_icon.source = 'icons/vegetable.png'
        self.ids.grains_icon.source = 'icons/grains.png'
        self.ids.protein_icon.source = 'icons/protein.png'
        self.ids.dairy_icon.source = 'icons/dairy.png'
        self.ids.more_icon.source = 'icons/more.png'
    pass

class ProfilePage(Screen):
    pass

class AccountPage(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    # validate
    def loginButton(self):
        if db.validate(self.username.text, self.password.text):
            self.reset()
            sm.current = "Homepage"
        else:
            invalidLogin()
    
    def createButton(self):
        self.reset()
        sm.current = "NewAccountPage"
    
    def reset(self):
        self.username.text = ""
        self.password.text = ""



class NewAccountPage(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def signup(self):
        if self.username.text != "":
            if self.password != "":
                db.add_user(self.username.text, self.password.text)

                self.reset()

                sm.current = "AccountPage"
            else:
                invalidForm()
        else:
            invalidForm()
    
    def login(self):
        self.reset()
        sm.current = "AccountPage"
    
    def reset(self):
        self.username.text = ""
        self.password.text = ""

                

class MealPlanPage(Screen):
    pass

class EditProfilePage(Screen):
    pass

class WindowManager(ScreenManager):
    pass


sm = WindowManager()
db = DataBase("users.txt")

class DFWS(MDApp):

    data = DictProperty()

    def floatButton(self):
        self.data = {
            'Create Meal': 'food'
        }  

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"


        return Builder.load_file('dfws.kv')



    # function that will display the weight
    def computeWeight(self, weight):
        if( weight < 0):
            weight = weight * (-1)
        elif( weight >= 10000):
            weight = 0

    weight = 10
    # function that would display the food weight 
    def displayWeight(self, weight):
        self.ids.weight_input.text = weight
        foodWeight = self.ids.weight_input.text


    # function that would display the calorie tracker
    def calorieTracker(self):
        current = self.ids.cal_tracker_bar.value
        # Start over after 100
        if current == 1:
            current = 0
        
        # Increment Value by calorie
        # Edit: test : .25
        current += .25
        # Update progress bar
        self.ids.cal_tracker_bar.value = current
        # Update Label
        self.ids.cal_tracker.text = f'{int(current*100)}% Progress'
            
def invalidLogin():
    pop = Popup(title = " Invalid Login ",
        content = Label (text = "Invalid username or password"),
        size_hint = (None, None),
        size = (400, 400)
    )
    pop.open()

def invalidForm():
    pop = Popup(title = " Invalid Form ",
        content = Label (text = "Fill in with valid information"),
        size_hint = (None, None),
        size = (400, 400)
    )
    pop.open()

if __name__ == '__main__':
    DFWS().run()
