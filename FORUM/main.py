from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from functools import partial
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.pagelayout import PageLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager
#from navigationdrawer import NavigationDrawer


# scroll ??? - layout in layout
# meniu

Window.size = (300,500)

class Scroll(ScrollView):
    pass

class MainWidget(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (228/255, 197/255, 175/255, 1)

        recenzii = []

    #imagine titlu
        titlu = Image(source='My travel app.png')
        self.add_widget(titlu)


        titlu_pagina = Label(text="Forum")
        titlu_pagina.color = (113 / 255, 165 / 255, 127 / 255, 1)
        titlu_pagina.font_size = "40dp"
        self.add_widget(titlu_pagina)

        # adaugare input oras
        oras = TextInput(text="Orasul tau...", multiline=False,size_hint=(0.7, 0.3),
                        pos_hint={'x': .15, 'y': .15})
        oras.background_color = (228/255, 197/255, 175/255, 1)
        oras.color = (113 / 255, 165 / 255, 127 / 255, 1)
        self.add_widget(oras)

        # adaugare input mesaj
        mesaj = TextInput(text="Mesajul tau...", multiline=True,size_hint=(0.7, 0.3),
                        pos_hint={'x': .15, 'y': .15})
        mesaj.color = (113 / 255, 165 / 255, 127 / 255, 1)
        mesaj.background_color = (228 / 255, 197 / 255, 175 / 255, 1)
        self.add_widget(mesaj)



        def afisare_recenzii():
            afisare_recenzii = ""
            for i in range(len(recenzii)):
                utilizator = "Anonim"
                recenzie = "\nRecenzie pentru orasul " + recenzii[i][0] + "\n de la utilizatorul " + utilizator+"\n" +recenzii[i][1]+"\n"

                afisare_recenzii += recenzie
                recenzii_afisate.text = afisare_recenzii

        def on_click(instance):
            recenzii.append((oras.text,mesaj.text))
            afisare_recenzii()

        # buton postare
        buton = Button(text="Posteaza !",size_hint=(0.7,0.2),
                        pos_hint={'x': .15, 'y': .15})
        buton.background_color = (7 / 255, 113 / 255, 135 / 255, 1)
        #buton.size_hint = 0.2,0.2
        buton.bind(on_press=on_click)

        self.add_widget(buton)


        recenzii_afisate = Label(text=" ")
        recenzii_afisate.color = (113 / 255, 165 / 255, 127 / 255, 1)
        self.add_widget(recenzii_afisate)


# TextInput:
# text: "Mesajul tau..."
# color: (113 / 255, 165 / 255, 127 / 255, 1)


class ForumApp(App):
    pass

ForumApp().run()

