from node import Node
from puzzle import *

from BuscasSemInformacao import *
from BuscasComInformacao import *
from Heuristicas import *

from util import *

print('Para ativar ou destivar os prints de debug utilize a flag PRINT_ATIVO no arquivo \'util.py\'')
printif('Prints de debug ativados......')

# Definindo no objetivo
obj = Puzzle(3, 3, [[1,2,3],[4,5,6],[7,8,None]])
objetivo = Node(obj)

# gerando nos aleatórios da profundidade 2 até 8
allstates = list()
for profundidade in range(2,9):
    # Dez estados de cada profundidade
    for k in range(10):
        # Definindo estado inicial
        raiz = Puzzle(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, None]])
        no_raiz = Node(raiz)

        visitados = [deepcopy(no_raiz)]
        p = 0
        novo = False
        while not novo or p < profundidade:
            moveu = no_raiz.state.move(randint(0,3))
            novo = no_raiz not in visitados
            if novo: # gerou novo estado, consequentemente moveu
                p += 1
                no_raiz.deepth = p
                visitados.append(deepcopy(no_raiz))
            elif moveu:  # moveu, mas n gerou novo estado
                for n in visitados:
                    if no_raiz == n:
                        p = n.deepth
                no_raiz.deepth = p
        no_raiz.heuristica = h2(no_raiz, objetivo)
        allstates.append(deepcopy(no_raiz))

time_0 = dt.datetime.now()
time_0 = time_0 - time_0
medias = {
    'gu_h1': [{'stored': 0, 'max_stored': 0, 'iterations': 0, 'time': time_0} for q in range(7)],
    'gu_h2': [{'stored': 0, 'max_stored': 0, 'iterations': 0, 'time': time_0} for q in range(7)],
    'ae_h1': [{'stored': 0, 'max_stored': 0, 'iterations': 0, 'time': time_0} for q in range(7)],
    'ae_h2': [{'stored': 0, 'max_stored': 0, 'iterations': 0, 'time': time_0} for q in range(7)],
}

for no in allstates:

    # armazenando profundidade para calculo do b*
    pr = no.deepth - 2
    # definindo profundidade do nó no inicio da busca
    no.deepth = 0

    ######### BuscaGulosa #########

    gulosa = BuscaGulosa(no, objetivo, h1)
    for key in medias['gu_h1'][pr]:
        if pr == 6:
            print('medias[\'gu_h1\'][',pr,'][',key,'] += ',gulosa[key],'/10')
        medias['gu_h1'][pr][key] += gulosa[key]/10 # divide por 10 para dar a media, pois sao 10 valores de cada profundidade (pr)
    # print_reponse(gulosa)

    gulosa = BuscaGulosa(no, objetivo, h2)
    for key in medias['gu_h2'][pr]:
        medias['gu_h2'][pr][key] += gulosa[key]/10 # divide por 10 para dar a media, pois sao 10 valores de cada profundidade (pr)
    # print_reponse(gulosa)

    ######### BuscaAE #########

    estrela = BuscaAEstrela(no, objetivo, h1)
    for key in medias['ae_h1'][pr]:
        medias['ae_h1'][pr][key] += estrela[key]/10 # divide por 10 para dar a media, pois sao 10 valores de cada profundidade (pr)
    # print_reponse(estrela)

    estrela = BuscaAEstrela(no, objetivo, h2)
    for key in medias['ae_h2'][pr]:
        medias['ae_h2'][pr][key] += estrela[key]/10 # divide por 10 para dar a media, pois sao 10 valores de cada profundidade (pr)
    # print_reponse(estrela)

print_avg_table(medias)
