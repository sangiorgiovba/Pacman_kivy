"""

Este é o código que exibirá uma foto na caixa central do jogo

"""
from kivy import require
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

require('1.9.1')# versão do Kivy usada neste script

class Photo(Widget):
    ph = StringProperty("Images/N.png")
    pass
