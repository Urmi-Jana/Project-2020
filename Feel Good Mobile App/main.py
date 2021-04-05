from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


Builder.load_file('design.kv')

class LoginScreen(Screen):
    def signup(self):
        self.manager.current = "sign_up_screen"
    def forgot(self):
        self.manager.current = "forgot_screen"
    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "loginsuccess"
        else:
            self.ids.login_wrong.text = "Wrong Username or Password"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, user, pword):
        with open("users.json") as file:
            users = json.load(file)
            
        
        users[user] = {'username' : user, 'password' : pword, 
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = "signup_success"

class ForgotScreen(Screen):
    def rep(self, user, pword):
        with open("users.json") as file:
            users = json.load(file)

        users[user] = {'username' : user, 'password' : pword, 
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = "signup_success" 

class SignUpSuccess(Screen):
    def login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename
                                 in available_feelings]
        
        if feel in available_feelings:
            file = open(f"quotes/{feel}.txt", encoding = "utf8")
            q = file.readlines()
            self.ids.quote.text = random.choice(q)
        else:
            self.ids.quote.text = "try another feeling"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
