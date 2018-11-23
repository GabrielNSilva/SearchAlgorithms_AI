import datetime as dt
from util import printif

def BuscaProfundidade(no_raiz, objetivo):

    ini = dt.datetime.now()
    it = 0
    max_len = 0
    pilha = list()
    pilha.append(no_raiz)

    while len(pilha):
        max_len = len(pilha) if len(pilha) > max_len else max_len
        
        it = it +1
        no = pilha.pop()

        if no == objetivo:
            return {'success': True, 'node': no, 'stored': len(pilha), 'max_stored': max_len, 'iterations': it, 'time': dt.datetime.now() - ini}
        
        for sucessor in no.get_sucessores():
            pilha.append(sucessor)

    return {'success': False, 'stored': len(pilha), 'max_stored': max_len, 'iterations': it, 'time': dt.datetime.now() - ini}
