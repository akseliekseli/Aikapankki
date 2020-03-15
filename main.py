from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.base import Builder
from kivy.properties import StringProperty
import requests
import json

class AlkuValikko(Screen):
    pass

class Aamupankki(Screen):
    url = "https://tjl-aikapankki.firebaseio.com/.json"
    auth_key = 'nCiheNSi6J1eSPLtEFhOMdBK8ipfLBorVEWsUbbG'
    response = requests.get(url + '?auth=' + auth_key)
    arvo = json.loads(response.text)
    saldo = arvo['Saldo']
    tulos = StringProperty(saldo)
    def on_pre_enter(self):
        url = "https://tjl-aikapankki.firebaseio.com/.json"
        auth_key = 'nCiheNSi6J1eSPLtEFhOMdBK8ipfLBorVEWsUbbG'
        response = requests.get(url + '?auth=' + auth_key)
        arvo = json.loads(response.text)
        saldo = arvo['Saldo']
        self.tulos = saldo
    
class Muutossivu(Screen):
    pass



class MainApp(App):
    url = "https://tjl-aikapankki.firebaseio.com/.json"
    auth_key = 'nCiheNSi6J1eSPLtEFhOMdBK8ipfLBorVEWsUbbG'
    response = requests.get(url + '?auth=' + auth_key)
    arvo = json.loads(response.text)
    saldo = arvo['Saldo']
    def build(self):
        GUI = Builder.load_file("main.kv")
        return GUI

    def change_screen(self, screen_name):
        #Otetaan screenmanager .kv tiedostosta
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

    def vahenna(self, saldo_muutos, salasana):
        if salasana == 'Jomppa':
            self.response = requests.get(self.url + '?auth=' + self.auth_key)
            self.arvo = json.loads(self.response.text)
            self.saldo = self.arvo['Saldo']
            self.arvo['Saldo'] = str( int(self.saldo) - int(saldo_muutos) )
            requests.patch(url=self.url, json=self.arvo)
    def lisaa(self, saldo_muutos, salasana):
        if salasana == 'Jomppa':
            self.response = requests.get(self.url + '?auth=' + self.auth_key)
            self.arvo = json.loads(self.response.text)
            self.saldo = self.arvo['Saldo']
            self.arvo['Saldo'] = str( int(self.saldo)+ int(saldo_muutos))
            requests.patch(url=self.url, json=self.arvo)  
    



MainApp().run()