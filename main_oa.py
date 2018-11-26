from node import Node
from puzzle import *
from BuscasSemInformacao import *
from BuscasComInformacao import *
from Heuristicas import *
from util import *

# obj = Puzzle(2, 2, [[1,2],[3,None]])
# objetivo = Node(obj)
# raiz = Puzzle(2, 2, [[1,2],[3,None]])
# no_raiz = Node(raiz)
# obj = Puzzle(3, 3, [[1,2,3],[4,5,6],[7,8,None]])
# objetivo = Node(obj)
# raiz = Puzzle(3, 3, [[1,2,3],[4,5,6],[7,8,None]])
# no_raiz = Node(raiz)
obj = Puzzle(3, 3, [[1,2,3],[4,5,6],[7,8,None]])
objetivo = Node(obj)
# raiz = Puzzle(3, 3, [[4,None,2],[5,6,8],[1,7,3]])
# raiz = Puzzle(3, 3, [[5,4,2],[1,6,8],[None,7,3]])
raiz = Puzzle(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, None]])
raiz = Puzzle(3, 3, [[3,7,1], [6,8,5], [4,None,2]])
no_raiz = Node(raiz)
# obj = Puzzle(5, 5, [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,None]])
# objetivo = Node(obj)
# raiz = Puzzle(5, 5, [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,None]])
# no_raiz = Node(raiz)

print('Para ativar ou destivar os prints de debug utilize a flag PRINT_ATIVO no arquivo \'util.py\'')
printif('Prints de debug ativados......')

# no_raiz.state.move(1)
# no_raiz.state.move(3)
# no_raiz.state.move(1)
# no_raiz.state.move(3)
# no_raiz.state.move(0)
# no_raiz.state.move(2)
# no_raiz.state.move(0)
# no_raiz.state.move(2)
# no_raiz.state.move(1)
# no_raiz.state.move(1)
# no_raiz.state.move(3)
# no_raiz.state.move(3)
# no_raiz.state.move(1)
# no_raiz.state.move(3)
# no_raiz.state.move(0)
# no_raiz.state.move(0)
# no_raiz.state.move(2)
# no_raiz.state.move(2)
# no_raiz.state.move(2)
# no_raiz.state.move(0)
# no_raiz.state.move(2)
# no_raiz.state.move(0)
# no_raiz.state.move(2)
# no_raiz.state.move(0)
# no_raiz.state.move(2)

############################################### BuscaLargura ###############################################

    # print()
    # print('-------------------------------------------------------')
    # print()
    # print('Raiz: ')
    # print(no_raiz.state)

    # largura = BuscaLargura(no_raiz, objetivo)
    # print('Largura:')
    # print_reponse(largura)

############################################### BuscaProfundidade ###############################################

    # print()
    # print('-------------------------------------------------------')
    # print()
    # print('Raiz: ')
    # print(no_raiz.state)

    # profundidade = BuscaProfundidade(no_raiz, objetivo)
    # print('Profundidade:')
    # print_reponse(profundidade)

############################################### BuscaProfundidadeLimitada ###############################################

    # print()
    # print('-------------------------------------------------------')
    # print()
    # print('Raiz: ')
    # print(no_raiz.state)

    # limitada = BuscaProfundidadeLimitada(no_raiz, objetivo, 20)
    # print('Profundidade Limitada:')
    # print_reponse(limitada)

############################################### BuscaAprofundamentoIterativo ###############################################

# print()
# print('-------------------------------------------------------')
# print()
# print('Raiz: ')
# print(no_raiz.state)

# iterarivo = BuscaAprofundamentoIterativo(no_raiz, objetivo)

# print('Aprofundamento Iterarivo:')
# print_reponse(iterarivo)

############################################### BuscaGulosa ###############################################

# print()
# print('-------------------------------------------------------')
# print()
# print('Raiz: ')
# print(no_raiz.state)

# gulosa = BuscaGulosa(no_raiz, objetivo, h1)

# print('Gulosa (h1):')
# print_reponse(gulosa)

# gulosa = BuscaGulosa(no_raiz, objetivo, h1)

# print('Gulosa (h2):')
# print_reponse(gulosa)

############################################### BuscaAE ###############################################

print()
print('-------------------------------------------------------')
print()
print('Raiz: ')
print(no_raiz.state)

# estrela = BuscaAEstrela(no_raiz, objetivo, h1)

# print('A* (h1):')
# print_reponse(estrela)

estrela = BuscaAEstrela(no_raiz, objetivo, h2)

print('A* (h2):')
print_reponse(estrela)
