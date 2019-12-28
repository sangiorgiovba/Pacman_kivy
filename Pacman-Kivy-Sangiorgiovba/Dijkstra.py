"""

Este script contém as funções que usamos para
Algoritmo de Dijkstra.

"""

########################################################################

###### Importes

#######################################################################

from heapq import *
import math

def distance(pointA, pointB):
    """Cálculo da distância euclidiana entre dois pontos do avião"""
    return math.sqrt((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)


def graphe(liste_de_voisins, liste_de_points):

    """Criação de um gráfico (na forma de um dicionário) usando uma lista de pontos
     e uma lista mostrando os pares / triplos de vizinhos"""

    gr={}
    for i in range(1,len(liste_de_voisins)+1):
        gr[i]=[]
        for j in liste_de_voisins[i-1]:
            gr[i].append((distance(liste_de_points[j],liste_de_points[i]), j))
    return(gr)

def voisins(s,graph):
    """ isso retorna os vizinhos do ponto s no gráfico gráfico"""
    return graph[s]

def dijkstra (s, t, graph):

    '''Implementamos o algoritmo Dijkstra usando o gráfico definido acima /
      Em seguida, calculamos a lista de pontos sucessivos que minimizam a distância (ponderada) entre o ponto se o ponto t'''

    M = set()
    d = {s: 0}
    p = {}
    suivants = [(0, s)]

    while suivants != []:

        dx, x = heappop(suivants)
        if x in M:
            continue

        M.add(x)

        for w, y in voisins(x,graph):
            if y in M:
                continue
            dy = dx + w
            if y not in d or d[y] > dy:
                d[y] = dy
                heappush(suivants, (dy, y))
                p[y] = x

    path = [t]
    x = t
    while x != s:
        x = p[x]
        path.insert(0, x)

    return d[t], path


def argmin(f, l, j):

    '''Esta função que usaremos mais tarde retorna o índice mínimo de uma lista'''

    arg = j
    for i in range(len(l)):
        if f(l[i]) < f(arg):
            arg = l[i]
    return arg
