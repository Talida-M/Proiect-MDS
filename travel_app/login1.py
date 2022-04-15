from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.context_instructions import Color
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import pandas as pd
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button

# logo

# nav bar

Window.size = (350, 600)
# Window.size = (300, 500)

# sectiune cu email, password, buton de "login" si buton de "register"
class LoginUI(Screen):
    # Window.color = (228/255, 197/255, 175/255, 1)
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    def on_login_click(self):
        # verificam daca email-ul exista in baza de date si daca avem o combinatie valida
        if self.email.text == "" or self.pwd.text == "":
            popup = Popup(title='Log In Error', content=Label(text='Invalid combination!'), size_hint=(None, None), size=(400, 400))
            popup.open()
        elif self.email.text not in users['Email'].unique():
            popup = Popup(title='Log In Error', content=Label(text='No user found!'), size_hint=(None, None), size=(400, 400))
            popup.open()
        else:
            # trecem la fereastra contului
            sm.current = 'logdata'
  
            # resetetam campurile de tip TextInput
            self.email.text = ""
            self.pwd.text = ""
    
    def go_to_register(self):
        sm.current = 'register'
    def on_forum_click(self):
        sm.current = 'forum'
    def on_signout_click(self):
        sm.current = 'login'

class Forum(Screen):
    def afisare_recenzie(self, rec, oras, label_afis_rec):
        if oras != "" and rec != "":
            rec_oras = pd.DataFrame([[oras, rec]], columns = ['Oras', 'Recenzie'])
            rec_oras.to_csv('travel_app/rec_orase.csv', mode = 'a', header = False, index = False)

            orase_recenzii = pd.read_csv('travel_app/rec_orase.csv')
            orase = orase_recenzii['Oras']
            recenzii = orase_recenzii['Recenzie']
            
            # afisare 
            afisare_recenzii = ""
            for i in range(len(recenzii)):
                utilizator = "Anonim"
                recenzie = "\nRecenzie pentru orasul " + orase[i] + "\n de la utilizatorul " + utilizator + "\n" + recenzii[i] + "\n"

                afisare_recenzii += recenzie
                label_afis_rec.text = afisare_recenzii
        
        else:
            popup = Popup(title='Review Error', content=Label(text='No review submitted'), size_hint=(None, None), size=(400, 400))
            popup.open()
    
    def on_signout_click(self):
        sm.current = 'login'
    
    def on_forum_click(self):
        sm.current = 'forum'


# clasa pentru a da switch intre ferestre
class windowManager(ScreenManager):
    pass

# sectiune cu mesaj si buton de "sign out"
class LogdataUI(Screen):
    Window.clearcolor = (0.92, 0.76, 0.63)
    def on_signout_click(self):
        sm.current = 'login'

# sectiune cu username, email, password, buton de "submit"
class RegisterUI(Screen):
    Window.clearcolor = (0.92, 0.76, 0.63)
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    def on_register_click(self):
        user = pd.DataFrame([[self.username.text, self.email.text, self.pwd.text]], columns = ['Username', 'Email', 'Password'])

        if self.email.text != "":
            if self.email.text not in users['Email'].unique():
                # daca email-ul nu exista deja in baza de date, adaugam noul user, si trecem la fereastra de log in
                user.to_csv('travel_app/login.csv', mode = 'a', header = False, index = False)
                sm.current = 'login'

                # resetam campurile
                self.username.text = ""
                self.email.text = ""
                self.pwd.text = ""
            else:
                popup = Popup(title='Sign Up Error', content=Label(text='User already exists!'), size_hint=(None, None), size=(400, 400))
                popup.open()
        else:
            # pentru campuri goale
            popup = Popup(title='Sign Up Error', content=Label(text='Invalid values'), size_hint=(None, None), size=(400, 400))
            popup.open()
    
    def on_signout_click(self):
        sm.current = 'login'
    
    def on_forum_click(self):
        popup = Popup(title='Not an user', content=Label(text='Please log in to access the forum!'), size_hint=(None, None), size=(500, 500))
        popup.open()

kv = Builder.load_file('travel_app/login1.kv')
sm = windowManager()

# stocam userii
users = pd.read_csv('travel_app/login.csv')
# print(users.keys())
  
# adaugam ecranele
sm.add_widget(LoginUI(name='login'))
sm.add_widget(RegisterUI(name='register'))
sm.add_widget(LogdataUI(name='logdata'))
sm.add_widget(Forum(name='forum'))

# clasa pentru gui
class loginMain(App):
    def build(self):
        return sm

loginMain().run()