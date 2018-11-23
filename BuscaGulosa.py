import datetime as dt
from util import printif

def BuscaGulosa(no_raiz, objetivo, heuristica):

    ini = dt.datetime.now()
    it = 0
    max_len = 0

    lista = list()
    # lista.append(no_raiz)
    no = no_raiz

    while true:
        max_len = len(lista) if len(lista) > max_len else max_len
        it = it + 1

        if no == objetivo:
            return no

        # comentar linha abaixo para ativar backtracking
        lista = list()
        for sucessor in no.get_sucessores():
            sucessor.heuristica = heuristica(sucessor)
            lista.append(sucessor)

        # busca na lista nó com menor heuristica
        for n in lista:
            no = n if n.heuristica < no.heuristica else no
        # n esqueca de retirar no da lista pq ele n vai mas ser folha
        lista.remove(no)