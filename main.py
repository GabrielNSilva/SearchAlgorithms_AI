from puzzle import Puzzle
from node import Node
from BuscaLargura import BuscaLargura
from BuscaProfundidade import BuscaProfundidade
from BuscaProfundidadeLimitada import BuscaProfundidadeLimitada
from BuscaAprofundamentoIterativo import BuscaAprofundamentoIterativo
from util import printif

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
no_raiz = Node(raiz)
# obj = Puzzle(5, 5, [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,None]])
# objetivo = Node(obj)
# raiz = Puzzle(5, 5, [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,None]])
# no_raiz = Node(raiz)

print('Para ativar ou destivar os prints de debug utilize a flag PRINT_ATIVO no arquivo \'util.py\'')
printif('Prints de debug ativados......')

no_raiz.state.move(1)
no_raiz.state.move(3)
no_raiz.state.move(1)
no_raiz.state.move(3)
no_raiz.state.move(0)
no_raiz.state.move(2)
no_raiz.state.move(0)
no_raiz.state.move(2)
#no_raiz.state.move(1)
#no_raiz.state.move(3)
#no_raiz.state.move(1)
#no_raiz.state.move(3)
#no_raiz.state.move(1)
#no_raiz.state.move(3)
#no_raiz.state.move(1)
#no_raiz.state.move(3)
#no_raiz.state.move(0)
#no_raiz.state.move(2)
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
    # if largura['success']:
    #     print('\t- Iterações: ' + str(largura['iterations']))
    #     print('\t- Tempo: ' + str(largura['time']))
    #     print('\t- Nodes armazenados (memória) [max]: ' + str(largura['max_stored']))
    #     print('\t- Nodes armazenados (memória) [fim]: ' + str(largura['stored']))
    #     print('\t- Node resposta: ' + str(largura['node']))
    #     print('\t- Caminho: ' + largura['node'].path())
    # else:
    #     print('Falhou!')
    #     print('\t- Iterações: ' + str(largura['iterations']))
    #     print('\t- Tempo: ' + str(largura['time']))
    #     print('\t- Nodes armazenados (memória) [max]: ' + str(largura['max_stored']))
    #     print('\t- Nodes armazenados (memória) [fim]: ' + str(largura['stored']))

############################################### BuscaProfundidade ###############################################

    # print()
    # print('-------------------------------------------------------')
    # print()
    # print('Raiz: ')
    # print(no_raiz.state)

    # profundidade = BuscaProfundidade(no_raiz, objetivo)
    # print('Profundidade:')
    # print('\t(Desativado pois entra em loop infinito)')
    # if profundidade['success']:
    #     print('\t- Iterações: ' + str(profundidade['iterations']))
    #     print('\t- Tempo: ' + str(profundidade['time']))
    #     print('\t- Nodes armazenados (memória) [max]: ' + str(profundidade['max_stored']))
    #     print('\t- Nodes armazenados (memória) [fim]: ' + str(profundidade['stored']))
    #     print('\t- Node resposta: ' + str(profundidade['node']))
    #     print('\t- Caminho: ' + profundidade['node'].path())
    # else:
    #     print('Falhou!')
    #     print('\t- Iterações: ' + str(profundidade['iterations']))
    #     print('\t- Tempo: ' + str(profundidade['time']))
    #     print('\t- Nodes armazenados (memória) [max]: ' + str(profundidade['max_stored']))
    #     print('\t- Nodes armazenados (memória) [fim]: ' + str(profundidade['stored']))

############################################### BuscaProfundidadeLimitada ###############################################

    # print()
    # print('-------------------------------------------------------')
    # print()
    # print('Raiz: ')
    # print(no_raiz.state)

    # limitada = BuscaProfundidadeLimitada(no_raiz, objetivo, 20)
    # print('Profundidade Limitada:')
    # if limitada['success']:
    #     print('\t- Iterações: ' + str(limitada['iterations']))
    #     print('\t- Tempo: ' + str(limitada['time']))
    #     print('\t- Nodes armazenados (memória) [max]: ' + str(limitada['max_stored']))
    #     print('\t- Nodes armazenados (memória) [fim]: ' + str(limitada['stored']))
    #     print('\t- Node resposta: ' + str(limitada['node']))
    #     print('\t- Caminho: ' + limitada['node'].path())
    # else:
    #     print('Falhou!')
    #     print('\t- Iterações: ' + str(limitada['iterations']))
    #     print('\t- Tempo: ' + str(limitada['time']))
    #     print('\t- Nodes armazenados (memória) [max]: ' + str(limitada['max_stored']))
    #     print('\t- Nodes armazenados (memória) [fim]: ' + str(limitada['stored']))

############################################### BuscaAprofundamentoIterativo ###############################################

print()
print('-------------------------------------------------------')
print()
print('Raiz: ')
print(no_raiz.state)

iterarivo = BuscaAprofundamentoIterativo(no_raiz, objetivo)

print('Aprofundamento Iterarivo:')

if iterarivo['success']:
    print('\t- Iterações: ' + str(iterarivo['iterations']))
    print('\t- Tempo: ' + str(iterarivo['time']))
    print('\t- Nodes armazenados (memória) [max]: ' + str(iterarivo['max_stored']))
    print('\t- Nodes armazenados (memória) [fim]: ' + str(iterarivo['stored']))
    print('\t- Node resposta: ' + str(iterarivo['node']))
    print('\t- Caminho: ' + iterarivo['node'].path())
else:
    print('Falhou!')
    print('\t- Iterações: ' + str(iterarivo['iterations']))
    print('\t- Tempo: ' + str(iterarivo['time']))
    print('\t- Nodes armazenados (memória) [max]: ' + str(iterarivo['max_stored']))
    print('\t- Nodes armazenados (memória) [fim]: ' + str(iterarivo['stored']))

print()
print('-------------------------------------------------------')
print()

############################################### BuscaGulosa ###############################################

print()
print('-------------------------------------------------------')
print()
print('Raiz: ')
print(no_raiz.state)

iterarivo = BuscaGulosa(no_raiz, objetivo)

print('Gulosa:')

if iterarivo['success']:
    print('\t- Iterações: ' + str(iterarivo['iterations']))
    print('\t- Tempo: ' + str(iterarivo['time']))
    print(
        '\t- Nodes armazenados (memória) [max]: ' + str(iterarivo['max_stored']))
    print('\t- Nodes armazenados (memória) [fim]: ' + str(iterarivo['stored']))
    print('\t- Node resposta: ' + str(iterarivo['node']))
    print('\t- Caminho: ' + iterarivo['node'].path())
else:
    print('Falhou!')
    print('\t- Iterações: ' + str(iterarivo['iterations']))
    print('\t- Tempo: ' + str(iterarivo['time']))
    print(
        '\t- Nodes armazenados (memória) [max]: ' + str(iterarivo['max_stored']))
    print('\t- Nodes armazenados (memória) [fim]: ' + str(iterarivo['stored']))

print()
print('-------------------------------------------------------')
print()

############################################### BuscaAE ###############################################

print()
print('-------------------------------------------------------')
print()
print('Raiz: ')
print(no_raiz.state)

iterarivo = BuscaAE(no_raiz, objetivo)

print('AE:')

if iterarivo['success']:
    print('\t- Iterações: ' + str(iterarivo['iterations']))
    print('\t- Tempo: ' + str(iterarivo['time']))
    print(
        '\t- Nodes armazenados (memória) [max]: ' + str(iterarivo['max_stored']))
    print('\t- Nodes armazenados (memória) [fim]: ' + str(iterarivo['stored']))
    print('\t- Node resposta: ' + str(iterarivo['node']))
    print('\t- Caminho: ' + iterarivo['node'].path())
else:
    print('Falhou!')
    print('\t- Iterações: ' + str(iterarivo['iterations']))
    print('\t- Tempo: ' + str(iterarivo['time']))
    print(
        '\t- Nodes armazenados (memória) [max]: ' + str(iterarivo['max_stored']))
    print('\t- Nodes armazenados (memória) [fim]: ' + str(iterarivo['stored']))

print()
print('-------------------------------------------------------')
print()
