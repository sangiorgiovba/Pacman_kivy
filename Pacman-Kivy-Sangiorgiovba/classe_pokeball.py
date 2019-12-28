"""

Criamos uma classe herdada da classe Widget e da qual o jogador é uma instância

"""

####################################################################################################

###Importes

####################################################################################################

from kivy import require
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

require('1.9.1')#versao do kivy que usamos para este script

####################################################################################################

###Classe do pokeball

####################################################################################################

class Pokeball(Widget):

    ima = StringProperty("Images/pokeball.png")

    def bounce_joueur(self, joueur):
        # Se o jogador entrar em contato com pokeball
        if self.x-10<= joueur.pos[0] and self.x+10>= joueur.pos[0] and self.y-30 == joueur.pos[1]:
            return True
        else:
            return False

# Testamos o contato entre o jogador e a pokeball
# Retornamos um booleano porque, para remover a pokeball (o widget), precisaremos fazer um teste booleen
