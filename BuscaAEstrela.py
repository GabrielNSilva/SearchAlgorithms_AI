import datetime as dt
from util import printif

def BuscaAEstrela(no_raiz, objetivo, heuristica):

    ini = dt.datetime.now()
    it = 0
    max_len = 0

    no_raiz.heuristica = heuristica(no_raiz, objetivo)
    folhas = list()
    visitados = list()
    visitados.append(no_raiz)
    no = no_raiz

    while True:
        max_len = len(folhas)+len(visitados) if len(folhas)+len(visitados) > max_len else max_len
        it = it + 1

        printif()
        # printif(folhas)

        printif('Iteracao ' + str(it))
        printif(no)

        if no == objetivo:
            return {'success': True, 'node': no, 'stored': len(folhas)+len(visitados), 'max_stored': max_len, 'iterations': it, 'time': dt.datetime.now() - ini}

        # comentar linha abaixo para ativar backtracking
        # folhas = list()
        for sucessor in no.get_sucessores():
            sucessor.heuristica = heuristica(sucessor, objetivo)
            if sucessor not in visitados:
                folhas.append(sucessor)

        # busca na lista de folhas o nó com menor heuristica
        no = folhas[0]
        for n in folhas:
            no = n if n.heuristica+n.cost < no.heuristica+no.cost else no
        # n esqueca de retirar no da lista pq ele n vai mas ser folha
        folhas.remove(no)
        visitados.append(no)