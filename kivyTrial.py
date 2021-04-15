import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import wolframalpha as wolfaplha
from kivy.uix.dropdown import DropDown
from kivy.uix.anchorlayout import AnchorLayout
import ssl

from kivy.core.window import Window
Window.clearcolor = (236/255,236/255,236/255,1)

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

class IntroPage(GridLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        self.rows = 4
    

        self.add_widget(Label(text="Welcome to Advance Calc", font_name = "Times New Roman", font_size = 60, color = [0,0,0,1]))
        self.calc_button = Button(text="Press to use Calculator", background_normal="",background_color = [247/255,136/255,136/255, 1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.calc_button.bind(on_press=self.calc_move)
        self.add_widget(self.calc_button)

        self.convert_button = Button(text="Press to use Covertor", background_normal="",background_color = [144/255,204/255,244/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40) 
        self.convert_button.bind(on_press=self.convt_move)
        self.add_widget(self.convert_button)

        self.advance_button = Button(text="Press to use Advance calc", background_normal="",background_color = [93/255,162/255,213/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40) 
        self.advance_button.bind(on_press=self.advCalc_move)
        self.add_widget(self.advance_button)

    def calc_move(self, instance):
        calc_app.screenmanager.current = "Calc"

    def convt_move(self, instance):
        calc_app.screenmanager.current = "Convt"

    def advCalc_move(self, instance):
        calc_app.screenmanager.current = "AdvCalc"

        

#intialising the calculator page that will appear after the clicking the 
#calculator button.
class CalcPage(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 6
        self.padding = 10
        self.spacing = 10
         
        #adding the text input box to enter the text 
        row1 = BoxLayout(orientation = "horizontal")
        self.entryText = TextInput(multiline="false", font_size = 50)
        row1.add_widget(self.entryText)
        self.add_widget(row1)

        #adding the first row of the button
        row2 = BoxLayout(orientation = "horizontal", spacing = "10")
        self.btn1 = Button(text="7", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn1.bind(on_press = self.num_7)
        self.btn2 = Button(text="8", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn2.bind(on_press=self.num_8)
        self.btn3 = Button(text="9", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn3.bind(on_press=self.num_9)
        self.btn4 = Button(text="+", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn4.bind(on_press = self.plus)
        row2.add_widget(self.btn1)
        row2.add_widget(self.btn2)
        row2.add_widget(self.btn3)
        row2.add_widget(self.btn4)
        self.add_widget(row2)

        #adding the second row of the button
        row3 = BoxLayout(orientation = "horizontal", spacing = "10")
        self.btn5 = Button(text="4", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn5.bind(on_press = self.num_4)
        self.btn6 = Button(text="5", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn6.bind(on_press = self.num_5)
        self.btn7 = Button(text="6", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn7.bind(on_press = self.num_6)
        self.btn8 = Button(text="-", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn8.bind(on_press = self.minus)
        row3.add_widget(self.btn5)
        row3.add_widget(self.btn6)
        row3.add_widget(self.btn7)
        row3.add_widget(self.btn8)
        self.add_widget(row3)

        #adding the third row of the button
        row4 = BoxLayout(orientation = "horizontal", spacing = "10")
        self.btn9 = Button(text="1", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn9.bind(on_press = self.num_1)
        self.btn10 = Button(text="2", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn10.bind(on_press = self.num_2)
        self.btn11 = Button(text="3", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn11.bind(on_press = self.num_3)
        self.btn12 = Button(text="*", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn12.bind(on_press = self.mult)
        row4.add_widget(self.btn9)
        row4.add_widget(self.btn10)
        row4.add_widget(self.btn11)
        row4.add_widget(self.btn12)
        self.add_widget(row4)

        #adding the fourth row of the button
        row5 = BoxLayout(orientation = "horizontal", spacing = "10")
        self.btn13 = Button(text="AC", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn13.bind(on_press = self.AC)
        self.btn14 = Button(text="0", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn14.bind(on_press = self.num_0)
        self.btn15 = Button(text="=", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn15.bind(on_press = self.equals)
        self.btn16 = Button(text="/", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn16.bind(on_press = self.div)
        row5.add_widget(self.btn13)
        row5.add_widget(self.btn14)
        row5.add_widget(self.btn15)
        row5.add_widget(self.btn16)
        self.add_widget(row5)

        #adding the final row
        row6 = BoxLayout(orientation = "horizontal", spacing = "10")
        self.btn17 = Button(text = "Back", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 )
        self.btn17.bind(on_press=self.back)
        row6.add_widget(self.btn17)
        self.add_widget(row6)

    #adding the functions to make the button and everything work
    def num_7(self, instance):
        self.entryText.text += self.btn1.text
    def num_8(self, instance):
        self.entryText.text += self.btn2.text
    def num_9(self, instance):
        self.entryText.text += self.btn3.text
    def plus(self, instance):
        self.entryText.text += self.btn4.text
    def num_4(self, instance):
        self.entryText.text += self.btn5.text
    def num_5(self, instance):
        self.entryText.text += self.btn6.text
    def num_6(self, instance):
        self.entryText.text += self.btn7.text
    def minus(self, instance):
        self.entryText.text += self.btn8.text
    def num_1(self, instance):
        self.entryText.text += self.btn9.text
    def num_2(self, instance):
        self.entryText.text += self.btn10.text
    def num_3(self, instance):
        self.entryText.text += self.btn11.text
    def mult(self, instance):
        self.entryText.text += self.btn12.text
    def AC(self, instance):
        self.entryText.text = ""
    def num_0(self, instance):
        self.entryText.text += self.btn14.text
    def equals(self, instance):
        try:
            self.entryText.text = str(eval(self.entryText.text))
        except:
            self.entryText.text = "Invalid! Press AC"
    def div(self, instance):
        self.entryText.text += self.btn16.text
    def back(self, instance):
        calc_app.screenmanager.current = "Intro"

#intialising the convertor page that will appear after clicking
#convert button
class ConvertPage(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 4
        self.padding = 10
        self.spacing = 10

         #adding the text input box to enter the text 
        row1 = BoxLayout(orientation = "horizontal")
        self.entryText = TextInput(multiline="false", font_size = 50)
        row1.add_widget(self.entryText)
        

#adding Type of units option.
        row1_2 = AnchorLayout(anchor_y="top")

        self.range = DropDown()

        self.rangeBtn = Button(text = "Type", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40,size_hint_y=None, height=60)
        self.rangeBtn.bind(on_release=self.range.open)

        self.type1 = Button(text = "length", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40,size_hint_y=None, height=60)
        self.type1.bind(on_release=lambda btn: self.range.select(self.type1.text))
        self.type1.bind(on_press = self.length_change)

        self.type2 = Button(text = "Time", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40,size_hint_y=None, height=60)
        self.type2.bind(on_release=lambda btn: self.range.select(self.type2.text))
        self.type2.bind(on_press = self.time_change)

        self.range.add_widget(self.type1)
        self.range.add_widget(self.type2)
        self.range.bind(on_select=lambda instance, x: setattr(self.rangeBtn, 'text', x))
        
        row1_2.add_widget(self.rangeBtn)
        row1.add_widget(row1_2)
        self.add_widget(row1)



#adding a vertical boxlayout
        row2 = BoxLayout(orientation = "horizontal", spacing = "10")
        self.LabelFrom = Label(text="From", font_name = "Times New Roman", font_size = 60, color = [0,0,0,1])
#adding a anchor layout to anchor the dropdown button to the top.        
        row2_1 = AnchorLayout(anchor_y="top")
#adding a from units drop down
        self.FromUnits = DropDown()
#adding the main button for the drop down
        self.fromBtn = Button(text = "From", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40,size_hint_y=None, height=60)
        self.fromBtn.bind(on_release=self.FromUnits.open)
#adding the first unit
        self.unit1_1 = Button(text = "_", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 ,size_hint_y=None, height=50) 
        self.unit1_1.bind(on_release=lambda btn: self.FromUnits.select(self.unit1_1.text))
        #self.unit1_1.bind(on_press = self.meter_unit)
#adding the second unit
        self.unit1_2 = Button(text = "_", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 ,size_hint_y=None, height=50) 
        self.unit1_2.bind(on_release=lambda btn: self.FromUnits.select(self.unit1_2.text))
        #self.unit1_2.bind(on_press = self.km_units)
        
#adding the third unit
        self.unit1_3 = Button(text = "_", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 ,size_hint_y=None, height=50) 
        self.unit1_3.bind(on_release=lambda btn: self.FromUnits.select(self.unit1_3.text))

#adding the third unit
        self.unit1_4 = Button(text = "_", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 ,size_hint_y=None, height=50) 
        self.unit1_4.bind(on_release=lambda btn: self.FromUnits.select(self.unit1_4.text))
#adding the buttons dropdown
        self.FromUnits.add_widget(self.unit1_1)
        self.FromUnits.add_widget(self.unit1_2)
        self.FromUnits.add_widget(self.unit1_3)
        self.FromUnits.add_widget(self.unit1_4)
        self.FromUnits.bind(on_select=lambda instance, x: setattr(self.fromBtn, 'text', x))
#adding the to label
        self.LabelTo = Label(text="To", font_name = "Times New Roman", font_size = 60, color = [0,0,0,1])

#adding a anchor layout to anchor the dropdown button to the top.        
        row2_2 = AnchorLayout(anchor_y="top")

#adding a from units drop down
        self.ToUnits = DropDown()
#adding the main button for the drop down
        self.toBtn = Button(text = "To", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40,size_hint_y=None, height=60)
        self.toBtn.bind(on_release=self.ToUnits.open)
#adding the first unit
        self.unit2_1 = Button(text = "_", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 ,size_hint_y=None, height=50) 
        self.unit2_1.bind(on_release=lambda btn: self.ToUnits.select(self.unit2_1.text))
#adding the second unit
        self.unit2_2 = Button(text = "_", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 ,size_hint_y=None, height=50) 
        self.unit2_2.bind(on_release=lambda btn: self.ToUnits.select(self.unit2_2.text))

#adding the third unit
        self.unit2_3 = Button(text = "_", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 ,size_hint_y=None, height=50) 
        self.unit2_3.bind(on_release=lambda btn: self.ToUnits.select(self.unit2_3.text))

#adding the third unit
        self.unit2_4 = Button(text = "_", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 ,size_hint_y=None, height=50) 
        self.unit2_4.bind(on_release=lambda btn: self.ToUnits.select(self.unit2_4.text))
#adding the buttons dropdown
        self.ToUnits.add_widget(self.unit2_1)
        self.ToUnits.add_widget(self.unit2_2)
        self.ToUnits.add_widget(self.unit2_3)
        self.ToUnits.add_widget(self.unit2_4)
        self.ToUnits.bind(on_select=lambda instance, x: setattr(self.toBtn, 'text', x))
    
#adding a convert button
        self.convert_button = Button(text="Convert", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.convert_button.bind(on_press = self.conversion)

#adding the widgets to the layouts.
       
        row2.add_widget(self.LabelFrom)
        row2_1.add_widget(self.fromBtn)
        row2.add_widget(row2_1)
        row2.add_widget(self.LabelTo)
        row2_2.add_widget(self.toBtn)
        row2.add_widget(row2_2)
        row2.add_widget(self.convert_button)
        self.add_widget(row2)


#adding the label for the result
        row3 = BoxLayout(orientation = "horizontal")
        self.resultLabel = Label(text="Result", font_name = "Times New Roman", font_size = 60, color = [0,0,0,1])
        row3.add_widget(self.resultLabel)
        self.add_widget(row3)




        #adding the final row
        row4 = BoxLayout(orientation = "horizontal")
        self.backBtn = Button(text = "Back", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 )
        self.backBtn.bind(on_press=self.back2)
        row4.add_widget(self.backBtn)
        self.add_widget(row4)
    
    def back2(self, instance):
        self.resultLabel.text = "Result"
        self.entryText.text = ""
        calc_app.screenmanager.current = "Intro"    
#adding function to change button names
    
    def km_units(self, instance):
        self.unit2_1.text = "mm"
        self.unit2_2.text = "m"

    def length_change(self,instance):
        self.unit1_1.text = "mm"
        self.unit1_2.text = "cm"
        self.unit1_3.text = "m"
        self.unit1_4.text = "Km"

        self.unit2_1.text = "mm"
        self.unit2_2.text = "cm"
        self.unit2_3.text = "m"
        self.unit2_4.text = "km"
    
    def time_change(self,instance):
        self.unit1_1.text = "ms"
        self.unit1_2.text = "s"
        self.unit1_3.text = "min"
        self.unit1_4.text = "hrs"

        self.unit2_1.text = "ms"
        self.unit2_2.text = "s"
        self.unit2_3.text = "min"
        self.unit2_4.text = "hrs"

    def conversion(self, instance):
        conversions = {
                "mm": {"mm": 1, "cm": 1/10, "m": 1/1000, "km": 1/1000000},
                "cm": {"mm": 10, "cm": 1, "m": 1/100, "km": 1/100000},
                "m":  {"mm": 1000, "cm": 100, "m": 1, "km": 1/1000},
                "km": {"mm": 100000, "cm": 10000, "m": 1000, "km": 1},
                "ms": {"ms": 1, "s" : 1/1000, "min" : 1/60000, "hrs": 1/36000000},
                "s" : {"ms": 1000, "s" : 1, "min" : 1/60, "hrs": 1/3600},
                "min": {"ms": 60000, "s" : 60, "min" : 1, "hrs": 1/60},
                "hrs" : {"ms": 3600000, "s" : 3600, "min" : 60, "hrs": 1},
              }
        
        try: 
            convert = conversions[self.fromBtn.text][self.toBtn.text]
        except KeyError:
            self.resultLabel.text = "Pls enter a valid conversion"
        
        self.resultLabel.text = str(int(self.entryText.text)*convert)

#intialising the Advance Calc page that will appear after clicking
#advance calc button
class AdvCalcPage(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 4
        self.padding = 10
        self.spacing = 10

        #adding the text input box to enter the text
        row1 = BoxLayout(orientation = "horizontal")
        self.inputText = TextInput(multiline="false", font_size = 50)
        row1.add_widget(self.inputText)
        self.add_widget(row1)

        #adding the button for retreving the result
        row2 = BoxLayout(orientation = "horizontal")
        self.btn1 = Button(text="Result", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman", color = [0,0,0,1], font_size =40)
        self.btn1.bind(on_press=self.WolfResult)
        row2.add_widget(self.btn1)
        self.add_widget(row2) 

        #adding the result label
        row3 = BoxLayout(orientation = "horizontal")
        self.wolfResult = Label(text="Results will appear here", font_name = "Times New Roman", font_size = 35, color = [0,0,0,1])
        #self.wolfResult.bind(width=self.update_text_width)
        row3.add_widget(self.wolfResult)
        self.add_widget(row3)

        #adding the final row
        row4 = BoxLayout(orientation = "horizontal", spacing = "10")
        self.backBtn = Button(text = "Back", background_normal = "", background_color = [153/255,206/255,211/255,1], font_name = "Times New Roman",color = [0,0,0,1], font_size =40 )
        self.backBtn.bind(on_press=self.back2)
        row4.add_widget(self.backBtn)
        self.add_widget(row4)
    
    def WolfResult(self, instance):
        app_id = 'GK5TVX-Q3KEU8J4HQ'
        client = wolfaplha.Client(app_id)
        result = client.query(self.inputText.text)
        try:
            answer = next(result.results).text
            self.wolfResult.text = answer
        except:
            answer = "This question is not valid"
            self.wolfResult.text = answer
        self.wolfResult.text_size = (self.wolfResult.width*0.9, None)
    
    def back2(self, instance):
        self.wolfResult.text = "Results will appear here"
        self.inputText.text = ""
        calc_app.screenmanager.current = "Intro"



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

        self.convt_page = ConvertPage()
        screen = Screen(name = "Convt")
        screen.add_widget(self.convt_page)
        self.screenmanager.add_widget(screen)

        self.advCalc_page = AdvCalcPage()
        screen = Screen(name = "AdvCalc")
        screen.add_widget(self.advCalc_page)
        self.screenmanager.add_widget(screen)



        return self.screenmanager

if __name__ == '__main__':
    calc_app = CalcApp()
    calc_app.run()