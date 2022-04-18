import csv

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
from bs4 import BeautifulSoup
import requests,openpyxl
import os
import webbrowser
import requests
#logo

#nav bar

Window.size = (350, 600)
# Window.size = (300, 500)


# sectiune cu email, password, buton de "login" si buton de "register"
class LoginUI(Screen):
    # Window.color = (228/255, 197/255, 175/255, 1)
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def on_login_click(self):

        user = pd.DataFrame([[self.email.text]],
                            columns=['Email'])

        # verificam daca email-ul exista in baza de date si daca avem o combinatie valida
        if self.email.text == "" or self.pwd.text == "":
            popup = Popup(title='Log In Error', content=Label(text='Invalid combination!'), size_hint=(None, None),
                          size=(400, 400))
            popup.open()
        elif self.email.text not in users['Email'].unique():
            popup = Popup(title='Log In Error', content=Label(text='No user found!'), size_hint=(None, None),
                          size=(400, 400))
            popup.open()
        elif self.email.text  in users['Email'].unique() and self.pwd.text not in users['Password'].unique():
            popup = Popup(title='Log In Error', content=Label(text='Incorrect Password!'), size_hint=(None, None),
                          size=(400, 400))
            popup.open()
        elif self.email.text  in users['Email'].unique():
            # trecem la fereastra contului
            #header email
            # with open('user.csv', 'w', newline='') as file:
            #     reader = csv.DictReader(file)
            #     with open('user.csv', 'w', newline='') as file:
            #         for line in reader:
            #             del line['Email']
            user.to_csv('user.csv', mode='a', header=False,
                        index=False)



            sm.current = 'profile'

            # resetetam campurile de tip TextInput
            self.email.text = ""
            self.pwd.text = ""

    def go_to_register(self):
        sm.current = 'register'

    def on_forum_click(self):
        sm.current = 'forum'

    def on_signout_click(self):
        sm.current = 'login'

    def on_myprofile_click(self):
        sm.current = 'profile'
    def on_home_click(self):
        sm.current = 'home'

class Forum(Screen):
    def afisare_recenzie(self, rec, oras, label_afis_rec):
        rec_oras = pd.DataFrame([[oras, rec]], columns=['Oras', 'Recenzie'])
        rec_oras.to_csv('rec_orase.csv', mode='a', header=False, index=False)

        orase_recenzii = pd.read_csv('rec_orase.csv')
        orase = orase_recenzii['Oras']
        recenzii = orase_recenzii['Recenzie']

        # afisare
        afisare_recenzii = ""
        for i in range(len(recenzii)):
            utilizator = "Anonim"
            recenzie = "\nRecenzie pentru orasul " + orase[i] + "\n de la utilizatorul " + utilizator + "\n" + recenzii[
                i] + "\n"

            afisare_recenzii += recenzie
            label_afis_rec.text = afisare_recenzii

    def on_signout_click(self):
        sm.current = 'login'

    def on_forum_click(self):
        sm.current = 'forum'

    def on_myprofile_click(self):
        sm.current = 'profile'
    def on_home_click(self):
        sm.current = 'home'


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
        user = pd.DataFrame([[self.username.text, self.email.text, self.pwd.text]],
                            columns=['Username', 'Email', 'Password'])

        if self.email.text != "":
            if self.email.text not in users['Email'].unique():
                # daca email-ul nu exista deja in baza de date, adaugam noul user, si trecem la fereastra de log in
                user.to_csv('login.csv', mode='a', header=False, index=False)
                sm.current = 'login'

                # resetam campurile
                self.username.text = ""
                self.email.text = ""
                self.pwd.text = ""
            else:
                popup = Popup(title='Sign Up Error', content=Label(text='User already exists!'), size_hint=(None, None),
                              size=(400, 400))
                popup.open()
        else:
            # pentru campuri goale
            popup = Popup(title='Sign Up Error', content=Label(text='Invalid values'), size_hint=(None, None),
                          size=(400, 400))
            popup.open()

class Filtre(Screen):
    def on_signout_click(self):
        sm.current = 'login'
    def on_myprofile_click(self):
        sm.current = 'profile'
    def on_forum_click(self):
        sm.current = 'forum'
    def on_home_click(self):
        sm.current = 'home'
    def afisare_zbor(self,email, oras, destinatie, plecare, sosire, buget, zbor_afisat):
        if email !="" and oras != "" and destinatie != "" and  plecare != "" and sosire != "" and buget != "":
            istoric = pd.DataFrame([[email, oras, destinatie, plecare, sosire, buget]], columns=['Email', 'Plecare Din', 'Destinatie',
                                                                                          'De cand', 'Pana cand', 'Buget'])
            istoric.to_csv('istoric.csv', mode='a', header=False, index=False)

            # istoric_zbor = pd.read_csv('istoric.csv')
            # orase = istoric_zbor['Plecare Din']
            # destinatii = istoric_zbor['Destinatie']
            # sosiri = istoric_zbor['De cand']
            # plecari = istoric_zbor['Pana cand']
            # bugete = istoric_zbor['Buget']
    def cazare_afisata(self, orasC, cazare, out, bug, cazari_afisate):
        if orasC != "" and cazare != "" and  out != "" and bug != "" :
            istoric = pd.DataFrame([[orasC, cazare, out, bug]], columns=['Oras', 'Check In', 'Check Out', 'Buget'])
            istoric.to_csv('istoricCazari.csv', mode='a', header=False, index=False)




class Home(Screen):

    def on_signout_click(self):
        sm.current = 'login'

    def on_forum_click(self):
        sm.current = 'forum'

    def on_home_click(self):
        sm.current = 'home'

    def on_filtre_click(self):
        sm.current = 'filtre'

    def go_to_register(self):
        sm.current = 'register'
    def on_myprofile_click(self):
        sm.current = 'profile'

    def on_buton1_click(self):
        webbrowser.open('https://travelzoom.ro/')
    def on_buton2_click(self):
        webbrowser.open('https://aventurescu.ro/')
    def on_buton3_click(self):
        webbrowser.open('https://lipa-lipa.ro/')
    def on_buton4_click(self):
        webbrowser.open('https://www.whisperwanderlust.com/ro/')

    def on_b_click(self):
        webbrowser.open('https://aventurescu.ro/weekend-prelungit-in-salonic-97-euro-zbor-cazare-3-nopti/')

    def on_bb_click(self):
        webbrowser.open('https://aventurescu.ro/vacanta-in-sardinia-107-euro-zbor-cazare-3-nopti/')

    def on_b_click(self):
        webbrowser.open('https://aventurescu.ro/city-break-de-3-zile-in-milano-75-euro-zbor-cazare/')





class Profile(Screen):

    def scraping(self):
        excel = openpyxl.Workbook()
        sheet = excel.active
        sheet.title = 'Top Rated Movies'
        sheet.append(['Rank', 'Movie', 'Year of Release', 'Rating'])
        try:
            #getting the html content of a webpage
            source=requests.get('https://www.imdb.com/chart/top-english-movies/')

            #in case the get request fails, the following line throws an error
            #for example if the path doesnt exist then its is going to return 404(not found)
            source.raise_for_status()

            # extracts the text out of my source object using the specified parser
            soup=BeautifulSoup(source.text,'html.parser')
            movies=soup.find('tbody',class_="lister-list").find_all('tr')

            for movie in movies:
                name=movie.find('td',class_="titleColumn").a.text
                rank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
                year=movie.find('td',class_="titleColumn").span.text.strip('()')
                rating=movie.find('td',class_="ratingColumn imdbRating").strong.text
                print(rank,name,year,rating)
                sheet.append([rank,name,year,rating])
        except Exception as e:
            print(e)
        excel.save('IMDB_movie_rating.xlsx')
    def show_movies(self,label_afis_mov):
        self.scraping()
        movies = pd.read_csv('IMDB_movie_rating.csv')
        rank = movies['Rank']
        name = movies['Movie']
        year = movies['Year of Release']
        rating = movies['Rating']

        # afisare
        get_movies = ""
        for i in range(len(movies)):

            line = str(rank[i])+ " "+ name[i] +" "+str(year[i])+ " " +str(rating[i])+ '\n'

            get_movies += line
            print(get_movies,"dsadasdasda")
            label_afis_mov.text = get_movies
        #movies.to_csv('/movies.csv', mode='a', header=False, index=False)
    def show_user_info(self,label_afis_user_info):
        user_info=pd.read_csv('user.csv')
        email = user_info['Email']
        print(email[1],type(email[1]))
        get_user_info=email

        label_afis_user_info.text=get_user_info[1]

        return get_user_info[1]

    def show_istoric_cautari(self,label_afis_istoric):
        current_user=self.show_user_info(label_afis_istoric)
        istoric_user = pd.read_csv('istoric.csv')

        email = istoric_user['Email']
        oras_s = istoric_user['Oras_Sursa']
        oras_d = istoric_user['Oras_Destinatie']
        data_p = istoric_user['Data_Plecare']
        data_i = istoric_user['Data_Intoarcere']
        buget = istoric_user['Buget']

        get_istoric = ""
        for i in range(len(istoric_user)):
            if email[i] == current_user:
                line = str(oras_s[i]) + " " + str(oras_d[i]) + " " + str(data_p[i]) + " " + str(data_i[i]) + " " + str(
                    buget[i])
                get_istoric += line

        label_afis_istoric.text = get_istoric
        # os.remove('user.csv')


    def on_myprofile_click(self):
        sm.current = 'profile'
    def go_to_register(self):
        sm.current = 'register'

    def on_forum_click(self):
        sm.current = 'forum'

    def on_signout_click(self):
        sm.current = 'login'

    def on_home_click(self):
        sm.current = 'home'


kv = Builder.load_file('login1.kv')
sm = windowManager()

# stocam userii
users = pd.read_csv('login.csv')
print(users.keys())

# adaugam ecranele
sm.add_widget(LoginUI(name='login'))
sm.add_widget(RegisterUI(name='register'))
sm.add_widget(LogdataUI(name='logdata'))
sm.add_widget(Forum(name='forum'))
sm.add_widget(Profile(name='profile'))
sm.add_widget(Home(name='home'))
sm.add_widget(Filtre(name='filtre'))

# clasa pentru gui
class loginMain(App):
    def build(self):

        return sm


loginMain().run()


"""def scrapping():
    try:
        # getting the html content of a webpage
        source = requests.get('https://www.imdb.com/chart/top/')
       # source = urllib.request.urlopen('http://www.momon...e&NA=false').read()
        # in case the get request fails, the following line throws an error
        # for example if the path doesnt exist then its is going to return 404(not found)
        source.raise_for_status()

        # extracts the text out of my source object using the specified parser
        soup = BeautifulSoup(source.text, 'html.parser')

        #print(soup.prettify())
       # print(soup)
        movies = soup.find('tbody',class_ ="lister-list").find_all('tr')
       #  altceva=movies.find('div',class_="anywhere-drawer")
       #  print(altceva)
       #  random_generated_id=altceva.find_all('div')
       #  newlist=[]
       #  for elem in random_generated_id:
       #      newlist.append(elem)
       #  asa=str(newlist).split("=")
       #  nr=2
       #  strnou=[]
       #  for litera in asa[1]:
       #      if litera=='"':
       #          nr-=1
       #      if nr==0:
       #          break
       #      if litera!='"':
       #          strnou.append(litera)
       #  id="".join(strnou)
       #  print(id)
       # # print(movies, "movies")
       #  oof = altceva.find('div',id=f'{id}')
       #  print(oof.text)


        for movie in movies:
            name = movie.find('td', class_="titleColumn").a.text
            rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
            year = movie.find('td', class_="titleColumn").span.text.strip('()')
            rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
            print(name, rank, year, rating)
    except Exception as e:
        print(e)

print(scrapping())"""