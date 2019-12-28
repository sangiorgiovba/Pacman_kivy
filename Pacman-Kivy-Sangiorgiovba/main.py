"""

Este é o nosso script principal que contém nosso aplicativo. É possível
inicie executando este script ou inicie o script "home.py" que abre um
página inicial redirecionando o usuário para este aplicativo.

"""

####################################################################

### 

#####################################################################

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '400')

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.label import Label
import time
from couloirs import *
from bouton_central import *
from fantome import *
from joueur import *
from points import *
from music import *
from classe_pokeball import *
from kivy.uix.screenmanager import Screen

require('1.9.1')# 

#####################################################################

### Classe de parede

#####################################################################
class Wall(Widget):
    pass

#####################################################################

###Classe de jogo Pacman

#####################################################################

class PacmanGame(Screen):

    """ Esta é a nossa aplicação, que é atualizada regularmente para levar em conta
     interação do usuário. Vamos instanciar os fantasmas, o jogador e o botão """

    partie = 'EN COURS'
    joueur = Player()
    gost1 = Fantome()
    gost2 = Fantome()
    photo = Photo()
    temps = 0
    liste_point = ['point{0}'.format(i) for i in range(0, len(point_a_manger))]

    def chrono(self,dt):
        '''O tempo é economizado quando essa função é chamada'''
        self.temps = time.time()

    def score_temps(self):
        '''Calculamos a pontuação adicional obtida com o tempo de jogo \
           Quanto mais rápido terminarmos o jogo, mais pontos ganharemos '''
        return (max([500-(time.time()-self.temps), 0]))

    #####################o teclado

    def __init__(self, **kwargs):
        super(PacmanGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'up':
            self.joueur.velocity=(0,1)
        elif keycode[1] == 'down':
            self.joueur.velocity=(0,-1)
        elif keycode[1] == 'left':
            self.joueur.velocity=(-1,0)
        elif keycode[1] == 'right':
            self.joueur.velocity=(1,0)
        return True

    #####################A função de atualização

    def update(self, dt):

        '''este método atualiza o jogo, entre o movimento do jogador, a estratégia dos fantasmas, etc. ...'''

        ## Enquanto o jogo está em andamento :
        if self.partie == 'EN COURS':
            self.joueur.move()
            self.joueur.move()

            #Se pegarmos a pokeball, a adicionaremos ao pokedex
            if self.pokeball.bounce_joueur(self.joueur):
                self.remove_widget(self.pokeball)
                self.joueur.pokedex = 1

            #Vemos se Sacha pega pontos brancos
            for i in reversed(range(len(ensemble))):
                if (self.joueur.pos[0] <= point_a_manger[ensemble[i]][0] - 20) and (
                    self.joueur.pos[0] >= point_a_manger[ensemble[i]][0] - 50) \
                        and (self.joueur.pos[1] <= point_a_manger[ensemble[i]][1] - 20) and (
                    self.joueur.pos[1] >= point_a_manger[ensemble[i]][1] - 50):
                    #Se sim, removemos o Widger do ponto, bem como sua posição na lista "juntos", e aumentamos a pontuação
                    self.remove_widget(globals()['point{0}'.format(ensemble[i])])
                    dico_points_voisins[ensemble[i]]=(dico_points_voisins[ensemble[i]][0],0)
                    del ensemble[i]
                    self.joueur.score += 1

                    #Se não houver mais pontos para comer, vencemos
                    if ensemble==[]:
                        self.partie = 'GAGNE'
                        self.joueur.score += ceil(self.score_temps())



            # Estamos interessados no contato entre Sacha e um fantasma, dependendo se ele tem uma pokeball ou não
            for gost in [self.gost1, self.gost2]:
                #Se não houver pokeball, sacha é comido e o jogo acaba
                if self.joueur.pokedex == 0:
                    if distance(self.joueur.pos, gost.pos) <= tx / 2:
                        self.remove_widget(self.joueur)
                        self.partie = 'GAME OVER'

                #caso contrário, Sacha pega o fantasma
                else:
                    if distance(self.joueur.pos, gost.pos) <= tx / 2:
                        self.remove_widget(gost)
                        self.add_widget(Pokeball(ima="Images/pokeball2.gif", pos=[gost.pos[0] + 20, gost.pos[1] + 20],
                                                 size=(50, 50)))
                        gost.pos = [0, 0]
                        del gost
                        self.joueur.pokedex = 0
                        #Comer um fantasma acrescenta pontos à pontuação
                        self.joueur.score += 200

        #se a festa acabar, paramos de jogar: dependendo de ganharmos ou perdermos, exibimos o rótulo e a pontuação de acordo
        else:
            if self.partie == 'GAME OVER':
                label = Label(text='GAME OVER\nSCORE={0}'.format(self.joueur.score), font_size=200)
                self.add_widget(label)
            else :
                label = Label(text='Vencedor\nSCORE={0}'.format(self.joueur.score), font_size=150)
                self.add_widget(label)

    def update_gost1(self,dt):
        '''Atualizamos a posição do 1º fantasma \
        1 vez que não evoluiu e até 3 vezes se estiver em sua última evolução (o fantasma será 3 vezes mais rápido)'''
        for i in range(self.gost1.evolution+1):
            self.gost1.strategie()

    def update_gost2(self,dt):
        '''Da mesma forma para o segundo fantasma, que tem uma estratégia diferente'''
        for i in range(self.gost2.evolution+1):
            self.gost2.strategie()

    def faire_strategie1(self,dt):
        '''Em seguida, atualizamos a estratégia que o primeiro fantasma deve seguir'''
        self.gost1.strategie_a_suivre(self.joueur.pt_proche)

    def faire_strategie2(self,dt):
        '''Em seguida, atualizamos a estratégia que o segundo fantasma deve seguir'''
        self.gost2.strategie_a_suivre2(self.joueur.pt_proche)

    def evolution(self,dt):
        ''' Fazemos os fantasmas evoluírem quando essa função é chamada'''
        if self.gost1.evolution ==0 and self.gost2.evolution ==0:
            self.gost1.evolution = 1
            self.gost2.evolution = 1
        else :
            self.gost1.evolution = 2
            self.gost2.evolution = 2

    def commencer(self):
        '''Começamos adicionando todos os widgets dos pontos no mapa, de acordo com a posição dada pela lista 'liste_a_manger' '''
        for i in range(0, len(point_a_manger)):
            if i != 179 and i != 170:
                globals()[self.liste_point[i]] = Points(pos=point_a_manger[i], size=(5, 5))
                self.add_widget(globals()[self.liste_point[i]])

#####################################################################

###Classe de aplicação

#####################################################################

class PacmanApp(App):
    '''Classe da nossa aplicação'''
    title = "Pacman - Jogo/Sangiorgiovba@gmail.com"
    debut = time.clock()
    def build(self):
        ''' Esse método cria o jogo, aciona as partidas dos fantasmas e atualiza a janela usando a função Clock.shedule_interval. '''
        game = PacmanGame()
        game.name = 'game'
        game.commencer()
        def retard(self):
            Clock.schedule_interval(game.update_gost2, 1.0 / 60.0)
        Clock.schedule_once(retard,15)
        Clock.schedule_interval(game.update_gost1, 1.0/60.0)
        Clock.schedule_interval(game.faire_strategie1, 5)
        Clock.schedule_interval(game.faire_strategie2, 5)
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        Clock.schedule_once(game.evolution, 50)
        Clock.schedule_once(game.evolution, 25)
        Clock.schedule_once(game.chrono)
        return game

#####################################################################

if __name__ == '__main__':
    PacmanApp().run()
