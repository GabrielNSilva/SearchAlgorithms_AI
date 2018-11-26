from puzzle import Puzzle
from node import Node
from Heuristicas import *
from copy import deepcopy

obj = Puzzle(3, 3, [[1,2,3],[4,5,6],[7,8,None]])
objetivo = Node(obj)
raiz = Puzzle(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, None]])
no_raiz = Node(raiz)

visitados = [deepcopy(no_raiz)]
p = 0
moveu = novo = False

moveu = no_raiz.state.move(1)
print(no_raiz)
novo = no_raiz not in visitados
p += novo and moveu  # se ambos true soma 1

print(novo)
print(moveu)
print(p)
