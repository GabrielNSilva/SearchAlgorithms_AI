import datetime as dt
from util import printif

def BuscaCustoUniforme(no_raiz, objetivo):

    ini = dt.datetime.now()
    it = 0
    max_len = 0

    lista = list()
    lista.append(no_raiz)

    while true:
        max_len = len(lista) if len(lista) > max_len else max_len
        it = it + 1

        if no == objetivo:
            return no

        for sucessor in no.get_sucessores():
            lista.append(sucessor)

        no = no com menor custo # busca na lista nó com menor custo
        # n esqueca de retirar no da lista pq ele n vai mas ser folha
