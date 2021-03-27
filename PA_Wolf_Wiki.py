import kivy
#import wikipedia
#import wolframalpha as wolfaplha
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput


class IntroPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text="Hello, welcome to the Assistant APP."))
        
        self.next_button = Button(text="Press to Continue",background_normal="", background_color=[1,.6,.2,.85])
        self.next_button.bind(on_press = self.continue_button)
        self.add_widget(self.next_button)

    def continue_button(self, instance):
        pa_app.screen_manager.current = "Choice"

class ChoicePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Wolfram Alpha"))

        self.add_widget(Label(text="Wikipedia"))

        self.wolf_button = Button(text="Press to use Wolfram Alpha", background_normal="",background_color = [1,.6,.2,1])
        self.wolf_button.bind(on_press=self.wolf_choice)
        self.add_widget(self.wolf_button)

        self.wiki_button = Button(text="Press to use Wikipedia", background_normal="",background_color = [.2,.6,1,1]) 
        self.wiki_button.bind(on_press=self.wiki_choice)
        self.add_widget(self.wiki_button)

    def wolf_choice(self, instance):
        pa_app.screen_manager.current = "Wolf"
    
    def wiki_choice(self, instance):
        pa_app.screen_manager.current = "Wiki"

class WolfPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Search Input:"))
        self.search_input = TextInput(multiline=False)
        self.add_widget(self.search_input)   

        self.sumbit_button = Button(text='Search',background_normal="", background_color=[1,.6,.2,.85])
        self.sumbit_button.bind(on_press=self.search_button)
        self.add_widget(Label())
        self.add_widget(self.sumbit_button)   

    def search_button(self, instance):
        app_id = 'GK5TVX-UPTWP79AWK'
        client = wolfaplha.Client(app_id)
        result = client.query(self.search_input.text)
        try:
            answer = next(result.results).text
            pa_app.result_page.update_info(answer)
            pa_app.screen_manager.current = "Result"
        except:
            error = "This question is not valid"
            pa_app.result_page.update_info(error)
            pa_app.screen_manager.current = "Result"

class  WikiPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Search Input:"))
        self.search_input = TextInput(multiline=False)
        self.add_widget(self.search_input)   

        self.sumbit_button = Button(text='Search',background_normal="", background_color=[1,.6,.2,.85])
        self.sumbit_button.bind(on_press=self.search_button)
        self.add_widget(Label())
        self.add_widget(self.sumbit_button)

    def search_button(self, instance):
        query = self.search_input.text
        try:
            results = wikipedia.summary(query, sentences=5)
        except:
            pass
        pa_app.result_page.update_info(results)
        pa_app.screen_manager.current = "Result"

class ResultPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="center", valign="middle", font_size=14)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

        self.exit_button = Button(text="Exit", background_normal="", background_color=[1,.6,.2,.85])
        self.exit_button.bind(on_press = self.exit)
        self.add_widget(self.exit_button)
    
    def exit(self, instance):
        pa_app.screen_manager.current = "Choice"

    
    def update_info(self, message):
        self.message.text = message
    
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)


class PaApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.intro_page = IntroPage()
        screen = Screen(name="Intro")
        screen.add_widget(self.intro_page)
        self.screen_manager.add_widget(screen)
        
        self.choice_Page = ChoicePage()
        screen = Screen(name="Choice")
        screen.add_widget(self.choice_Page)
        self.screen_manager.add_widget(screen)

        self.wolf_page = WolfPage()
        screen = Screen(name="Wolf")
        screen.add_widget(self.wolf_page)
        self.screen_manager.add_widget(screen)

        self.wiki_page = WikiPage()
        screen = Screen(name="Wiki")
        screen.add_widget(self.wiki_page)
        self.screen_manager.add_widget(screen)

        self.result_page = ResultPage()
        screen = Screen(name="Result")
        screen.add_widget(self.result_page)
        self.screen_manager.add_widget(screen)
    
        return self.screen_manager

if __name__ == "__main__":
    pa_app = PaApp()
    pa_app.run()
