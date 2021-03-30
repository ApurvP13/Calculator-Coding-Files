import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class IntroPage(GridLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        self.rows = 4
    

        self.add_widget(Label(text="Welcome to Advance Calc", font_name = "Times New Roman"))
        self.calc_button = Button(text="Press to use Calculator", background_normal="",background_color = [228/255,132/255,0,1])
        self.calc_button.bind(on_press=self.calc_move)
        self.add_widget(self.calc_button)

        self.convert_button = Button(text="Press to use Covertor", background_normal="",background_color = [96/255,130/255,182/255,1]) 
        #self.wiki_button.bind(on_press=self.wiki_choice)
        self.add_widget(self.convert_button)

        self.advance_button = Button(text="Press to use Advance calc", background_normal="",background_color = [115/255, 134/255, 120/255, 1]) 
        #self.wiki_button.bind(on_press=self.wiki_choice)
        self.add_widget(self.advance_button)

    def calc_move(self, instance):
        calc_app.screenmanager.current = "Calc"
        

#intialising the calculator page that will appear after the clicking the 
#calculator button.
class CalcPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 6
         
        #adding the text input box to enter the text 
        row1 = BoxLayout(orientation = "horizontal")
        entryText = TextInput(multiline="false")
        row1.add_widget(entryText)
        self.add_widget(row1)

        #adding the first row of the button
        row2 = BoxLayout(orientation = "horizontal", spacing = "10")
        btn1 = Button(text="7")
        btn2 = Button(text="8")
        btn3 = Button(text="9")
        btn4 = Button(text="+")
        row2.add_widget(btn1)
        row2.add_widget(btn2)
        row2.add_widget(btn3)
        row2.add_widget(btn4)
        self.add_widget(row2)

        #adding the second row of the button
        row3 = BoxLayout(orientation = "horizontal", spacing = "10")
        btn5 = Button(text="4")
        btn6 = Button(text="5")
        btn7 = Button(text="6")
        btn8 = Button(text="-")
        row3.add_widget(btn5)
        row3.add_widget(btn6)
        row3.add_widget(btn7)
        row3.add_widget(btn8)
        self.add_widget(row3)

        #adding the third row of the button
        row4 = BoxLayout(orientation = "horizontal", spacing = "10")
        btn9 = Button(text="1")
        btn10 = Button(text="2")
        btn11 = Button(text="3")
        btn12 = Button(text="*")
        row4.add_widget(btn9)
        row4.add_widget(btn10)
        row4.add_widget(btn11)
        row4.add_widget(btn12)
        self.add_widget(row4)

        #adding the fourth row of the button
        row2 = BoxLayout(orientation = "horizontal", spacing = "10")
        btn1 = Button(text="7")
        btn2 = Button(text="8")
        btn3 = Button(text="9")
        btn4 = Button(text="+")
        row2.add_widget(btn1)
        row2.add_widget(btn2)
        row2.add_widget(btn3)
        row2.add_widget(btn4)
        self.add_widget(row2)





        



class CalcApp(App):
    def build(self):
        self.screenmanager = ScreenManager()

        self.intro_page = IntroPage()
        screen = Screen(name = "Intro")
        screen.add_widget(self.intro_page)
        self.screenmanager.add_widget(screen)

        self.calc_page = CalcPage()
        screen = Screen(name = "Calc")
        screen.add_widget(self.calc_page)
        self.screenmanager.add_widget(screen)


        return self.screenmanager

if __name__ == '__main__':
    calc_app = CalcApp()
    calc_app.run()