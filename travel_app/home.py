from bokeh.models import TextInput
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.rst import RstDocument
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList

Window.size = (350, 600)

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


        titlu_pagina = Label(text="Home")
        titlu_pagina.color = (113 / 255, 165 / 255, 127 / 255, 1)
        titlu_pagina.font_size = "40dp"
        self.add_widget(titlu_pagina)

        # adaugare input oras
        oras = TextInput(hint_text="Plecare Din", multiline=False,size_hint=(0.7, 0.3),
                        pos_hint={'x': .15, 'y': .15},
                         width= "200dp",
                    height ="25dp")
        oras.background_color = (228/255, 197/255, 175/255, 1)
        oras.color = (113 / 255, 165 / 255, 127 / 255, 1)
        self.add_widget(oras)

        # adaugare input mesaj
        mesaj = TextInput(text="Mesajul tau...", multiline=True,size_hint=(0.7, 0.3),
                        pos_hint={'x': .15, 'y': .15})
        mesaj.color = (113 / 255, 165 / 255, 127 / 255, 1)
        mesaj.background_color = (228 / 255, 197 / 255, 175 / 255, 1)
        self.add_widget(mesaj)






# TextInput:
# text: "Mesajul tau..."
# color: (113 / 255, 165 / 255, 127 / 255, 1)


class HomeApp(App):
    pass

HomeApp().run()