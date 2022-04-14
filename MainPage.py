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

navigation_helper = """
Screen:            
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    opacity:0.8
                    canvas.before:
                        Rectangle:
                            source:'logo.jpeg'
                            size: root.width, root.height
                            pos: self.pos
                    
                    MDToolbar:
                        title: "Meniu"
                        background_color: (113 / 255, 165 / 255, 127 / 255, 1)
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        elevation:5
                    Label:
                        text: "Alege cum vrei sa calatoresti:"
                        font_size: 14
                        color: (7/255, 79/255, 87/255)
                        background_color: (1, 1, 1,1)
                        halign: 'left'
                        allow_stretch: True
                        keep_ratio: True
                        canvas.before:
                            Color:
                                rgba: self.background_color
                        pos_hint:{'x': .02, 'y': 0.5}
                        bold: True
                        italic: True
                        outline_color: (1,1,1)
                        outline_width: 10
                    TextInput:
                        text: "Din"
                        size_hint:(0.7, 0.3)
                        background_color: (228/255, 197/255, 175/255, 1)
                        pos_hint:{'x': .15, 'y': .15}
                    TextInput:
                        text: "Spre"
                        size_hint:(0.7, 0.3)
                        background_color: (228/255, 197/255, 175/255, 1)
                        pos_hint:{'x': .15, 'y': .15}
                    TextInput:
                        text: "Data Plecare"
                        size_hint:(0.7, 0.3)
                        background_color: (228/255, 197/255, 175/255, 1)
                        pos_hint:{'x': .15, 'y': .15}
                    TextInput:
                        text: "Data Sosire"
                        size_hint:(0.7, 0.3)
                        background_color: (228/255, 197/255, 175/255, 1)
                        pos_hint:{'x': .15, 'y': .15}
                    TextInput:
                        text: "Buget"
                        size_hint:(0.7, 0.3)
                        background_color: (228/255, 197/255, 175/255, 1)
                        pos_hint:{'x': .15, 'y': .15}
                    Button:
                        text:"Filtreaza !"
                        size_hint:(0.7,0.2)
                        pos_hint:{'x': .15, 'y': .15}
                        background_color: (7 / 255, 113 / 255, 135 / 255, 1)
                    BoxLayout:
                        Label:
                            text: "Inspiratii pentru vacanta:"
                            font_size: 18
                            color: (7/255, 79/255, 87/255)
                            background_color: (1, 1, 1,1)
                            text_size: self.size     
                            halign: 'center'
                            valign: 'bottom'
                            padding_y: 10
                            allow_stretch: True
                            keep_ratio: True
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                            bold: True
                            italic: True
                            outline_color: (1,1,1)
                            outline_width: 10 
                    Label:
                        text: "Aventurescu: https://aventurescu.ro/"
                        font_size: 16
                        color: (7/255, 79/255, 87/255)
                        background_color: (1, 1, 1,1)
                        size_hint:(0.4, 0.3)
                        padding_y: 10
                        valign: 'center'
                        pos_hint:{'x': 0.23, 'y': .10}
                        allow_stretch: True
                        keep_ratio: True
                        canvas.before:
                            Color:
                                rgba: self.background_color
                            
                        bold: True
                        italic: True
                        outline_color: (1,1,1)
                        outline_width: 10           
                        
                    Label:
                        text: "Imperator Travel: https://www.imperatortravel.ro/"
                        font_size: 14
                        color: (7/255, 79/255, 87/255)
                        background_color: (1, 1, 1,1)
                        size_hint:(0.4, 0.3)
                        padding_y: 10
                        valign: 'center'
                        pos_hint:{'x': 0.25, 'y': .10}
                        allow_stretch: True
                        keep_ratio: True
                        canvas.before:
                            Color:
                                rgba: self.background_color
                            
                        bold: True
                        italic: True
                        outline_color: (1,1,1)
                        outline_width: 10 
                    Label:
                        text: "Lipa Lipa: https://lipa-lipa.ro/"
                        font_size: 14
                        color: (7/255, 79/255, 87/255)
                        background_color: (1, 1, 1,1)
                        size_hint:(0.4, 0.3)
                        padding_y: 10
                        valign: 'center'
                        pos_hint:{'x': 0.25, 'y': .10}
                        allow_stretch: True
                        keep_ratio: True
                        canvas.before:
                            Color:
                                rgba: self.background_color
                            
                        bold: True
                        italic: True
                        outline_color: (1,1,1)
                        outline_width: 10         
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (0.7,0.6)
                    source: "menu.jpg"
                MDLabel:
                    text: "Start Your Adventure"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    DrawerList:
                        id: md_list
                        
                        MDList:
                            OneLineIconListItem:
                                text: "Forum"
                            
                                IconLeftWidget:
                                    icon: "comment-edit"
                                    
                           
                                    
                            OneLineIconListItem:
                                text: "Login"
                            
                                IconLeftWidget:
                                    icon: "airport"
                                    
                           
                            OneLineIconListItem:
                                text: "Logout"
                            
                                IconLeftWidget:
                                    icon: "logout"
                                  
                           
                                
                            
                            
"""

text = """
Screen:
    MainWidget:
        BoxLayout:
              Label:
                font_size: 16
                background_color: (158/255, 206/255, 154/255,1)
                canvas.before:
                Color:
                    rgba: self.background_color
                Rectangle:
                    size: self.size
                    pos: self.pos 
                # Text Properties
                color: (0,1,0,1)
                bold: True
                italic: True
                outline_color: (0,0,1)
                outline_width: 10

"""
Window.clearcolor = (0.92, 0.76, 0.63)
class Background(BoxLayout):
    def build(self):
        _long_text = """Călătorii! Fie că-ți vizitezi  familia  în mediul rural, fie că zbori 

                în  Grecia, poți avea parte de aventuri oriunde în lume!

               Călătoriile au  atât de multe beneficii, inclusiv îmbunătățirea

               unei limbi noi, învățarea istoriei locului și a  diverselor

                informații, dar cel mai important este crearea unor  amintiri de

               neuitat, care pot fi împărtășite cu prietenii, familia sau copiii 

               în viitor. Tocmai de aceea, va recomandam 10 blogg-uri de calatorie

               care va vor inspira in alegerea unei locatii:
               https://aventurescu.ro/

               https://www.imperatortravel.ro/

               https://lipa-lipa.ro/

               https://dailytravelpill.com/

               https://designedtotravel.ro/

               https://consilierturism.ro/

               https://travelista.ro/

               https://travelzoom.ro/

               https://www.whisperwanderlust.com/ro/

               https://blog.travelminit.ro/"""
        return RstDocument(text=_long_text)



class MainPageApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    class MainWidget(BoxLayout):
        pass

    def build(self):

        screen = Builder.load_string(navigation_helper)

        return screen
    Background()


    def on_start(self):
        pass


MainPageApp().run()
#GridLayout