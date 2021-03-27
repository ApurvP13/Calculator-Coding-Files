from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button

class IntroPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        self.rows = 4

        self.add_widget(Label(text="Welcome to Advance Calc"))
        self.calc_button = Button(text="Press to use Calculator", background_normal="",background_color = [228/255,132/255,0,1])
        #self.wolf_button.bind(on_press=self.wolf_choice)
        self.add_widget(self.calc_button)

        self.convert_button = Button(text="Press to use Covertor", background_normal="",background_color = [96/255,130/255,182/255,1]) 
        #self.wiki_button.bind(on_press=self.wiki_choice)
        self.add_widget(self.convert_button)

        self.advance_button = Button(text="Press to use Advance calc", background_normal="",background_color = [115/255, 134/255, 120/255, 1]) 
        #self.wiki_button.bind(on_press=self.wiki_choice)
        self.add_widget(self.advance_button)


class CalcApp(App):
    def build(self):
        self.screenmanager = ScreenManager()

        self.intro_page = IntroPage()
        screen = Screen(name = "Intro")
        screen.add_widget(self.intro_page)
        self.screenmanager.add_widget(screen)


        return self.screenmanager

if __name__ == '__main__':
    calc_app = CalcApp()
    calc_app.run()