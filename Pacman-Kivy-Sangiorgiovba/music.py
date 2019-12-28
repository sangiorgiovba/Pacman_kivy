"""

Este script permite que você tenha uma roda para gerenciar o volume da música.

"""

####################################################################

###

#####################################################################

from kivy import require
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.uix.slider import Slider
from kivy.app import App

require('1.8.0')

class Volume_Slider(Widget):
    def __init__(self, **kwargs):
        super(Volume_Slider, self).__init__(**kwargs)
        s = SoundLoader.load("Musiques/Monody.mp3")
        slider = Slider(value=s.volume, min=0, max=1, orientation='vertical')
        s.play()
        s.bind(volume=slider.setter('value'))
        slider.bind(value=s.setter('volume'))
        self.add_widget(slider)


class MyApp(App):
    def build(self):
        return Volume_Slider()

if __name__ == '__main__':
    MyApp().run()
#(# OLA DE VOLTA COM O JOGO EM KIVY , CAMO VCS JA SABE FLEI NO
# ULTIMO VIDEO ONDE NOS CONCLUIMOS O JGO DO MEMORIA ENIGMA
# EU MISTUREI ALGUNS CODIGO , OU SEJA EU ESTAVA EM OUTRO PC E 
# ACABEI CONFUNDINDO TUDO CREI ALGUMAS VARIAVEIS PENSANDO QUE
# ESTAVA NO ARQUIVO DO MEMORIA ENIGMA E NA VERDADE ESTAVA NO 
# ARQUIVO DO KIVY ETC , MAIS AQUI TEM PRECISEI FAZER ALGUMAS
# ALTERACOES DEVIDO ESTE ERRO AI ,,, BOM O QUE VIMOS 
# NOS VIDEO E O MESMO PROCEDIMENTO AQUI ... INCLUSIVE NO
# VIDEO ANTERIOR EU NAO TINHA AINDA CRIADO O ARQUIVO .KIVY
# VAMOS REVER ELE AGORA JA ESTA PRONTO
# VOU DEIXAR UMA COPIA DETALHADO NO GIT PARA VCS CONFERIR 
# VAMOS EXECUTAR ESTE GAME
# SEMPRE PELO ARQUIVO HOME.PY )
