"""

Criamos uma classe herdada da classe Widget e da qual o jogador é uma instância

"""

####################################################################################################

###Importes

####################################################################################################

from kivy import require
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,StringProperty
from kivy.vector import Vector
from couloirs import dpoint, couloir, liste_voisins
from Dijkstra import distance, argmin

require('1.9.1')#
####################################################################################################

###

####################################################################################################

class Player(Widget):

    """O jogador é controlado pelo usuário usando as setas direcionais e deve absorver os pontos.
     Não pode atravessar paredes e deve evitar entrar em contato com fantasmas.
     O jogador se move horizontal e verticalmente nos pontos
     do gráfico. Absorve moedas para ganhar pontos, é bloqueado por paredes
     e deve evitar fantasmas """

    pokedex=0
    pt_proche = 1
    score = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    elan = (0, 0)
    velocity = ReferenceListProperty(velocity_x, velocity_y) 
    im = StringProperty("Images/sacha_front.gif")

    def move(self):

        """ Método que avança o jogador através do labirinto """

        ancienne_pos = self.pos.copy()
        for corr in couloir :
            if (corr[0] <= self.velocity_x + self.pos[0]) and (corr[2] >= self.velocity_x + self.pos[0]) and \
                    (corr[1] <= self.velocity_y + self.pos[1]) and (corr[3] >= self.velocity_y + self.pos[1]):
                self.pos = Vector(*self.velocity)+self.pos
                self.elan = self.velocity.copy()
                if self.velocity == [0, 1]:
                    self.im = "Images/sacha_back.gif"
                elif self.velocity == [0, -1]:
                    self.im = "Images/sacha_front.gif"
                elif self.velocity == [-1, 0]:
                    self.im = "Images/sacha_left.gif"
                elif self.velocity == [1, 0]:
                    self.im = "Images/sacha_right.gif"
        if self.pos == ancienne_pos:
            for corr in couloir:
                 if (corr[0] - 0.1 <= self.elan[0] + self.pos[0]) and (corr[2] + 0.1 >= self.elan[0] + self.pos[0]) and \
                         (corr[1] - 0.1 <= self.elan[1] + self.pos[1]) and (corr[3] + 0.1 >= self.elan[1] + self.pos[1]):
                    self.pos = Vector(*self.elan) + self.pos

        if self.pos == [dpoint[27][0], (dpoint[27][1])]:
            self.pos = [dpoint[30][0], (dpoint[30][1])]

        elif self.pos == [dpoint[30][0], (dpoint[30][1])]:
            self.pos =[dpoint[27][0], (dpoint[27][1])]

        #Calculamos o ponto do gráfico mais próximo do Pac-Man
        self.pt_proche = \
            argmin(lambda x: distance(self.pos, dpoint[x]),liste_voisins[self.pt_proche - 1], self.pt_proche)
