from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from navigationdrawer import NavigationDrawer
from navigationdrawer import NavigationDrawer
Config.set('kivy', 'window_icon', 'icon.ico')

Window.size = (350, 600)
stilizare = '''
#:import Toolbar kivymd.toolbar.Toolbar

BoxLayout:
    orientation: 'vertical'
    Toolbar:
        id: toolbar
        title: 'Start your adventure'
        background_color: app.theme_cls.primary_light
        left_action_items: [['menu', lambda x: app.nav_drawer.toggle()]]
        right_action_items: [['more-vert', lambda x: app.raised_button.open(self.parent)]]
    Label:
<Navigator>:
    NavigationDrawerIconButton:
        icon: 'airplane'
        text: 'Login'
    NavigationDrawerIconButton:
        icon: 'airport'
        text: 'Sign Up'
    NavigationDrawerIconButton:
        icon: 'earth'
        text: 'Forum'
    NavigationDrawerIconButton:
        icon: 'settings'
        text: 'Settings'
    '''

class MyLayout(BoxLayout):
    pass

class MainWidget(Widget):
    Window.clearcolor = (0.92, 0.76, 0.63)


class Navigator(NavigationDrawer):
    pass

class MainPageApp(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        self.theme_cls.primary_palette = "Green"
        main_widget = Builder.load_string(stilizare)
        return main_widget

MainPageApp().run()
#GridLayout