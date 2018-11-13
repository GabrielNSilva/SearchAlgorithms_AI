from queue import Queue
import datetime as dt
from util import printif

def BuscaAprofundamentoIterativo(no_raiz, objetivo, lim_ini=0):

    ini = dt.datetime.now()
    it = 0
    max_len = 0
    lim = lim_ini

    while(True):
        printif('================================> Limite ' + str(lim))
        pilha = list()
        pilha.append(no_raiz)

        while len(pilha):
            max_len = len(pilha) if len(pilha) > max_len else max_len

            printif()
            printif(pilha)
            
            it = it +1
            no = pilha.pop()
            
            printif('Profundidade ' + str(no.deepth) + '/' + str(lim))
            printif(no)

            if no == objetivo:
                return {'success': True, 'node': no, 'stored': len(pilha), 'max_stored': max_len, 'iterations': it, 'time': dt.datetime.now() - ini}
            
            if no.deepth < lim:
                for sucessor in no.get_sucessores():
                    pilha.append(sucessor)

        # Fail -- Tentar mais fundo
        lim = lim +1
