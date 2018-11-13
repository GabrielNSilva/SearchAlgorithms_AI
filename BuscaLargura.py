from queue import Queue
import datetime as dt
from util import printif

def BuscaLargura(no_raiz, objetivo):

    ini = dt.datetime.now()
    it = 0
    max_len = 0
    fila = Queue()
    fila.put(no_raiz)

    while not fila.empty():
        max_len = fila.qsize() if fila.qsize() > max_len else max_len
        
        it = it +1
        no = fila.get()

        if no == objetivo:
            return {'success': True, 'node': no, 'stored': fila.qsize(), 'max_stored': max_len, 'iterations': it, 'time': dt.datetime.now() - ini}
        
        for sucessor in no.get_sucessores():
            fila.put(sucessor)
        # print(fila.queue)
        # return False

    return {'success': False, 'stored': fila.qsize(), 'max_stored': max_len, 'iterations': it, 'time': dt.datetime.now() - ini}
