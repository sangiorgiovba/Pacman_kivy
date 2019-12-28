"""

Este script permite ter uma página inicial antes de iniciar o jogo.

"""

####################################################################

### Importes

#####################################################################
from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '400')

#As instruções a seguir permitem definir o tamanho mínimo da janela, em caso de redimensionamento, retorne a este tamanho
from kivy.core.window import Window
Window.minimum_width = 1200
Window.minimum_height = 400

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,FallOutTransition
from main import *
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

####################################################################

### Arquivo .kv da janela inicial

#####################################################################

Builder.load_string("""
#:import Volume_Slider music.Volume_Slider

<Persos>:
    Image:
		source: root.im
		pos: root.pos
        size: 76, 76

<MenuScreen>:
    perso1: ectoplasma
    perso2: spectrum
    perso3: fantominus
    perso4: sacha

    canvas:
        Rectangle:
            source: "Images/background_bis.png"
            size: self.size
            pos: self.pos

    Persos:
        id: ectoplasma
        pos: 320,37

    Persos:
        id: spectrum
        pos: 397,37

    Persos:
        id: fantominus
        pos: 464,37

    Persos:
        id: sacha
        pos: 541,37

    Button:
        size_hint: 0.25,0.25
        pos: 20,37
        background_normal: "Images/jouer.png"
        on_press: root.manager.current_screen.add_widget(root.gaming.build()) ; root.manager.current_screen.add_widget(Volume_Slider())

    Button:
        size_hint: 0.20, 0.20
        pos: 880, 37
        text: "Regras Do Jogo"
        font_size: 30
        color: 162 / 255, 185 / 255, 245 / 255, 1
        background_color: 14 / 255, 18 / 255, 98 / 255, 1
        on_press: root.pop.open()

""")

#####################################################################

###As classes visíveis na tela inicial

#####################################################################
b = BoxLayout(orientation='vertical', spacing=10)
p = Popup(title='Regras Do Jogo : SANGIORGIOVBA@GMAIL.COM / TODOS OS DIREITOS RESERVADOS', title_size=30, title_color=[0 / 255, 255 / 255, 0/ 255, 1], \
          content=b, auto_dismiss=False, separator_color = [0/ 255, 255 / 255, 0/ 255, 1])
l = Button(text = 'Entendi', size_hint = (1, 0.2))
l.bind(on_press=p.dismiss)
b.add_widget(Label(text = "                      O jogo que você vai jogar é semelhante ao Pacman, mas algumas regras diferem no entanto: \
                               \n\n                      -O objetivo do jogo é consumir todos os pontos em branco do jogo.O jogo termina assim que todos os pontos em branco são consumidos e sua pontuação é exibida.\
                               \n\n                      -Se um fantasma te pega, o jogo acaba. Cuidado, os fantasmas evoluem e a velocidade deles aumenta. \
                               \n\n                      -Você notará a presença de uma pokeball: agarrando-a, você pode pegar um dos dois fantasmas. \
                               \n\n                      Mas cuidado, há apenas uma pokeball no campo, considere-a, uma vez na mão, como uma vida de alívio!\
                               \n\n                      -Seu tempo é precioso, quanto mais rápido você ganha, maior sua pontuação !\
                               \n\n                      Voila, use as setas para se movimentar e que a sorte esteja com você !"))
b.add_widget(l)

class Persos(Widget):

    ''' Criamos a classe de caracteres que podemos ver na tela inicial. \
     Esses caracteres servem como animação quando você está na página inicial'''

    photo_im = [StringProperty(""), StringProperty("")]
    im=photo_im[0]
    velocity_x = NumericProperty(2)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    avance = 260

    def move(self):
        if self.avance > 0:
            self.pos = Vector(*self.velocity) + self.pos
            self.avance -= 2
        else:
            self.velocity_x = - self.velocity_x
            self.avance = 260
            self.im = self.photo_im[min(int(self.velocity_x / abs(self.velocity_x)), 0)]


class MenuScreen(Screen):

    ''' Definimos a tela de boas-vindas '''

    perso1 = Persos()
    perso2 = Persos()
    perso3 = Persos()
    perso4 = Persos()
    gaming = PacmanApp()
    gaming.load_kv()

    def photo(self):
        self.perso1.photo_im = ["Images/ectoplasma_right.gif", "Images/ectoplasma_left.gif"]
        self.perso1.im = self.perso1.photo_im[0]
        self.perso2.photo_im = ["Images/spectrum_right.gif", "Images/spectrum_left.gif"]
        self.perso2.im = self.perso2.photo_im[0]
        self.perso3.photo_im = ["Images/fantominus_right.gif", "Images/fantominus_left.gif"]
        self.perso3.im = self.perso3.photo_im[0]
        self.perso4.photo_im = ["Images/sacha_right.gif", "Images/sacha_left.gif"]
        self.perso4.im = self.perso4.photo_im[0]

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.pop = p


    def update(self, dt):
        self.perso1.move()
        self.perso2.move()
        self.perso3.move()
        self.perso4.move()

class TestApp(App):
    title = "Pacman - Jogo/Sangiorgiovba@gmail.com :"
    def build(self):
        sm = ScreenManager(transition=FallOutTransition(duration=0.1))
        men = MenuScreen(name='menu')
        sm.add_widget(men)
        men.photo()
        Clock.schedule_interval(men.update, 1.0 / 6000.0)
        return sm

#####################################################################

if __name__ == '__main__':
    TestApp().run()
