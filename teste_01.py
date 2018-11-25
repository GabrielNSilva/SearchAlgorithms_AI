from puzzle import Puzzle
from node import Node
from Heuristicas import *
obj = Puzzle(3, 3, [[1,2,3],[4,5,6],[7,8,None]])
objetivo = Node(obj)
raiz = Puzzle(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, None]])
no_raiz = Node(raiz)
no_raiz.state.move(1)
no_raiz.state.move(3)
no_raiz.state.move(1)
no_raiz.state.move(3)
no_raiz.state.move(0)
no_raiz.state.move(2)
no_raiz.state.move(0)

print(objetivo)
print(no_raiz)

print(h1(no_raiz, objetivo))
print(h2(no_raiz, objetivo))

no_raiz.state.move(2)

print(objetivo)
print(no_raiz)

print(h1(no_raiz, objetivo))
print(h2(no_raiz, objetivo))