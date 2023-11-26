from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
        
        # استخدام BoxLayout بتوجيه أفقي (orientation='horizontal')
        layout = GridLayout(cols=4, rows=2)

        self.label = Label(text="Label 1", font_size=30)
        layout.add_widget(self.label)

        self.button = Button(text="Screen 2")
        self.button.bind(on_press=self.switch_to_screen_two)
        layout.add_widget(self.button)

        self.add_widget(layout)
        
        layout.size_hint = (0.55, 0.25)
        layout.center_x = 100
        layout.center_y = 300


    def switch_to_screen_two(self, instance):
        self.manager.current = 'screen2'

class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        
        # استخدام BoxLayout بتوجيه أفقي (orientation='vertical')
        layout = GridLayout(cols=4, rows=2)

        self.label = Label(text="Label 2", font_size=30)
        layout.add_widget(self.label)

        self.button = Button(text="Screen 1")
        self.button.bind(on_press=self.switch_to_screen_one)
        layout.add_widget(self.button)

        self.add_widget(layout)
        layout.size_hint = (0.55, 0.25)
        layout.center_x = 100
        layout.center_y = 300

    def switch_to_screen_one(self, instance):
        self.manager.current = 'screen1'

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        screen1 = ScreenOne(name='screen1')
        screen2 = ScreenTwo(name='screen2')
        sm.add_widget(screen1)
        sm.add_widget(screen2)

        sm.current = 'screen1'
       

        return sm

if __name__ == '__main__':
    MyApp().run()
