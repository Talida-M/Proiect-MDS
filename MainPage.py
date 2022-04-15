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
                    BoxLayout:    
                        Button:
                            text:"Login"
                            size_hint:(0.5,0.2)
                            pos_hint:{'x': 1.0, 'y': 0.7}
                            background_color: (7 / 255, 113 / 255, 135 / 255, 1)
                            
                        Button:
                            text:"Register"
                            size_hint:(0.5,0.2)
                            pos_hint:{'x': 1.0, 'y': 0.7}
                            background_color: (7 / 255, 113 / 255, 135 / 255, 1)
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
                        hint_text: "Plecare Din"
                        id: plecare
                        multiline: False
                        size_hint: None, None
                        width: "200dp"
                        height: "25dp"
                        pos_hint: {"center_x": 0.5}
                        background_color: (228 / 255, 197 / 255, 175 / 255, 1)
                        
                    TextInput:
                        hint_text: "Locatie"
                        id: locatie
                        multiline: False
                        size_hint: None, None
                        width: "200dp"
                        height: "25dp"
                        pos_hint: {"center_x": 0.5}
                        background_color: (228 / 255, 197 / 255, 175 / 255, 1)
                    TextInput:
                        hint_text: "Data Plecare"
                        id: data1
                        multiline: False
                        size_hint: None, None
                        width: "200dp"
                        height: "25dp"
                        pos_hint: {"center_x": 0.5}
                        background_color: (228 / 255, 197 / 255, 175 / 255, 1)
                    TextInput:
                        hint_text: "Data Sosire"
                        id: data2
                        multiline: False
                        size_hint: None, None
                        width: "200dp"
                        height: "25dp"
                        pos_hint: {"center_x": 0.5}
                        background_color: (228 / 255, 197 / 255, 175 / 255, 1)
                    TextInput:
                        hint_text: "Buget"
                        id: buget
                        multiline: False
                        size_hint: None, None
                        width: "200dp"
                        height: "25dp"
                        pos_hint: {"center_x": 0.5}
                        background_color: (228 / 255, 197 / 255, 175 / 255, 1)
                    Button:
                        text:"Filtreaza !"
                        size_hint:(0.7,0.2)
                        pos_hint:{'x': .15, 'y': .15}
                        background_color: (7 / 255, 113 / 255, 135 / 255)
                    ScrollView:    
                        Label:
                            text: "Ajuta-ne sa iti gasim cazarea perfecta:"
                            font_size: 14
                            color: (7/255, 79/255, 87/255)
                            background_color: (1, 1, 1,1)
                            halign: 'left'
                            allow_stretch: True
                            keep_ratio: True
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                            pos_hint:{'x': .04, 'y': 0.7}
                            bold: True
                            italic: True
                            outline_color: (1,1,1)
                            outline_width: 10    
                    TextInput:
                        hint_text: "Oras"
                        id: oras
                        multiline: False
                        size_hint: None, None
                        width: "200dp"
                        height: "25dp"
                        pos_hint: {"center_x": 0.5}
                        background_color: (228 / 255, 197 / 255, 175 / 255, 1)
                    TextInput:
                        hint_text: "Data Cazare"
                        id: dataC
                        multiline: False
                        size_hint: None, None
                        width: "200dp"
                        height: "25dp"
                        pos_hint: {"center_x": 0.5}
                        background_color: (228 / 255, 197 / 255, 175 / 255, 1)
                    TextInput:
                        hint_text: "Data Plecare"
                        id: dataP
                        multiline: False
                        size_hint: None, None
                        width: "200dp"
                        height: "25dp"
                        pos_hint: {"center_x": 0.5}
                        background_color: (228 / 255, 197 / 255, 175 / 255, 1)
                    TextInput:
                        hint_text: "Buget"
                        id: buget
                        multiline: False
                        size_hint: None, None
                        width: "200dp"
                        height: "25dp"
                        pos_hint: {"center_x": 0.5}
                        background_color: (228 / 255, 197 / 255, 175 / 255, 1)
                    Button:
                        text:"Cauta Cazare !"
                        size_hint:(0.7,0.2)
                        pos_hint:{'x': .15, 'y': .15}
                        background_color: (7 / 255, 113 / 255, 135 / 255, 1)
                    ScrollView:
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
                        pos_hint:{'x': 0.4, 'y': .10}
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
                        pos_hint:{'x': 0.5, 'y': .10}
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
                        pos_hint:{'x': 0.6, 'y': .1}
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
    pass



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