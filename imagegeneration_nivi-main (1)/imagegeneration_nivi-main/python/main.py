from kivy import *
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout


Window.clearcolor = (0, 0.1, 0.22, 2)
class MyApp(App):  
    def build(self):
        layout = FloatLayout()      
        icon_image = Image(source='cropnv.png', size_hint=(None, None), size=(100, 100),pos_hint={'center_x':0.48,'center_y':0.9})
        layout.add_widget(icon_image)
        
        highlight_label = Label(text="NIVI", font_size=45, color=(30,30,30),bold=True,pos_hint={'center_x':0.52,'center_y':0.9})
        layout.add_widget(highlight_label)
        button = Button(text='NIVI', font_size=10,background_color=(0.1, 0.1, 0.10, 1),size_hint=(None,None),size=(50,50),pos_hint={'center_x':0.5,'center_y':0.5})
        button.bind(on_press=self.button_pressed)
        layout.add_widget(button)
        mike=Image(source="btmike.png",size_hint=(None, None), size=(200, 200),pos_hint={'center_x':0.5,'center_y':0.5} )
        mike.bind(on_press=self.button_pressed)
        layout.add_widget(mike)
        link_icon=Image(source="soundwave.png",size_hint=(None, None), size=(300, 300),pos_hint={'center_x':0.5,'center_y':0.4} )
        layout.add_widget(link_icon)
        speak_text = Label(text="Tap to speak", font_size=22, color=(30,30,30),pos_hint={'center_x':0.5,'center_y':0.3})
        layout.add_widget(speak_text)
        link_icon=Image(source="instalogo.png",size_hint=(None, None), size=(70, 70),pos_hint={'center_x':0.6,'center_y':0.11} )
        layout.add_widget(link_icon)
        link_icon=Image(source="linkedinlogo.png",size_hint=(None, None), size=(65, 65),pos_hint={'center_x':0.7,'center_y':0.1} )
        layout.add_widget(link_icon)
        link_icon=Image(source="twitterlogo.png",size_hint=(None, None), size=(60, 60),pos_hint={'center_x':0.8,'center_y':0.1} )
        layout.add_widget(link_icon)
        link_icon=Image(source="githublogo.png",size_hint=(None, None), size=(65, 65),pos_hint={'center_x':0.9,'center_y':0.1} )
        layout.add_widget(link_icon)
        return layout  
    def button_pressed(self, instance):
        import nivi as neural_vision 
        neural_vision()        
        
        



    

        
    
MyApp().run()
