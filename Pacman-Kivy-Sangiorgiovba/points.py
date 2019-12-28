"""

Criamos uma classe herdada da classe Widget e cujas paredes são uma instância

"""

####################################################################################################

###Importes

####################################################################################################

from kivy import require
from kivy.uix.widget import Widget
from couloirs import couloir
from Dijkstra import *
from couloirs import *

require('1.9.1')

####################################################################################################

###

####################################################################################################

point_a_manger = []
# lista de coordenadas dos pontos que o jogador deve absorver

for a0, a1, b0, b1 in couloir:
    if a0 == b0:
        for j in range(int(a1) + 20, int(b1) - 20, 20):
            #Pontos espaçados regularmente são colocados nos corredores verticais)
            point_a_manger.append([a0 + 38.5, j + 38.5])
            #Centramos os pontos
    else:
        for j in range(int(a0), int(b0), 20):
            #Pontos espaçados regularmente são colocados nos corredores horizontais
            point_a_manger.append([j + 38.5, a1 + 38.5])

point_a_manger = point_a_manger[:191]
#Nós nos restringimos aos primeiros 191 pontos brancos (ou seja, de 0 a 190), não queremos pontos na passagem secreta

ensemble = [i for i in range(len(point_a_manger)) if i not in [179, 170]]
# a lista "set" será usada para atualizar os pontos brancos que permanecem no jogo. Removeremos elementos dessa lista à medida que o jogo avança.

ens_point= ensemble.copy()
#Criamos uma cópia de "set" para ter todos os pontos brancos. Esta lista será usada para calcular a pontuação da 2ª estratégia fantasma

def voisins_points():

    ''' Essa função nos permite criar um dicionário que associa a cada ponto branco a lista de pontos brancos vizinhos a menos de 60 pixels de distância '''

    dico_points_voisins = {}
    for i in ensemble:
        l = []
        for j in ensemble:
            if j != i and distance(point_a_manger[i], point_a_manger[j]) <= 60:
                l.append(j)
        dico_points_voisins[i]=(l,1)
    return dico_points_voisins

dico_points_voisins = voisins_points()


def pls_pr_voisins_pt():

    '''  Função que associa a cada ponto branco o ponto do gráfico mais próximo \
      Isso também nos ajudará com as estratégias dos fantasmas que funcionam nos pontos do gráfico'''

    dico={}
    for i in ens_point:
        coord=point_a_manger[i]
        proche = 1
        dist = distance(dpoint[1], coord)
        for j in range(1,31):
            if distance(dpoint[j],point_a_manger[i])<dist:
                proche=j
                dist=distance(dpoint[j],point_a_manger[i])
        dico[i]=proche
    return dico

dico_pls_pr_voisins_point= pls_pr_voisins_pt()
#Agora temos o dicionário de pontos do gráfico mais próximo dos pontos brancos para comer


####################################################################################################

###

####################################################################################################

class Points(Widget):

    """ Os pontos permitem ao jogador aumentar sua pontuação e terminar o jogo"""

    def bounce_joueur(self, joueur):

        """ Se o jogador entrar em contato com o ponto """

        if [self.x-38.5, self.y-38.5] == joueur.pos:
            return True
        else:
            return False
