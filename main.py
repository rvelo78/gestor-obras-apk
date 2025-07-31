from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
import os
import datetime

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text='Gestor de Obras RV', font_size='24sp'))
        layout.add_widget(Label(text='Usuario:'))
        self.user_input = TextInput(multiline=False)
        layout.add_widget(self.user_input)
        
        layout.add_widget(Label(text='Contraseña:'))
        self.pass_input = TextInput(password=True, multiline=False)
        layout.add_widget(self.pass_input)
        
        login_btn = Button(text='Ingresar')
        login_btn.bind(on_press=self.do_login)
        layout.add_widget(login_btn)
        
        self.error_label = Label(text='', color=(1, 0, 0, 1))
        layout.add_widget(self.error_label)
        
        self.add_widget(layout)
    
    def do_login(self, instance):
        if self.user_input.text == 'admin' and self.pass_input.text == 'admin':
            self.manager.current = 'main'
        else:
            self.error_label.text = 'Usuario o contraseña incorrectos'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'main'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text='Gestor de Obras RV\nVersión Android', font_size='20sp'))
        
        btn_obras = Button(text='Gestión de Obras')
        btn_tareas = Button(text='Tareas')
        btn_materiales = Button(text='Materiales')
        btn_logout = Button(text='Cerrar Sesión')
        btn_logout.bind(on_press=self.logout)
        
        layout.add_widget(btn_obras)
        layout.add_widget(btn_tareas)
        layout.add_widget(btn_materiales)
        layout.add_widget(btn_logout)
        
        self.add_widget(layout)
    
    def logout(self, instance):
        self.manager.current = 'login'

class GestorObrasApp(App):
    def build(self):
        self.title = 'Gestor de Obras RV'
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(MainScreen())
        
        return sm

GestorObrasApp().run()