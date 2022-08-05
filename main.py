from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.core.window import Window


Window.clearcolor = (.35, .35, .35, 1)


class YuyushaApp(App):

    def build(self):

        MainBox = BoxLayout(
            padding = (5,10,10,10),
            orientation = "horizontal"
            )
        MainBox.clearcolor = (.52, .52, .52, 1)

        MenuBox = BoxLayout(
            orientation = "vertical",
            size_hint = (None, 1),
            height = "220dp",
            width = "70dp",
            )
        MenuBox.add_widget(Button(text = "q", size_hint = (None, None), height = "70dp", width = "70dp"))
        MenuBox.add_widget(Button(text = "q", size_hint = (None, None), height = "70dp", width = "70dp"))
        MenuBox.add_widget(Widget(size_hint = (1, 1)))
        MainBox.add_widget(MenuBox)

        MainGrid = GridLayout(rows=5, spacing = 5, padding = (5,0,0,0))
        for i in range(25):
            MainGrid.add_widget(Button(text=str(i)))

        MainBox.add_widget(MainGrid)

        return MainBox

if __name__ == "__main__":
    YuyushaApp().run()