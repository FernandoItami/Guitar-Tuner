import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class TunerApp(App):

    def build(self):
        return GridLayout()

tunApp = TunerApp()
tunApp.run()