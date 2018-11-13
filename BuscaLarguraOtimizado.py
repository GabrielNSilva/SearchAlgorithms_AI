from queue import Queue
import datetime as dt

def BuscaLarguraOtimizado(no_raiz, objetivo):

    ini = dt.datetime.now()
    it = 0
    if no_raiz == objetivo:
        return {'node': no_raiz, 'stored': 1, 'iterations': it, 'time': dt.datetime.now() - ini}

    fila = Queue()
    fila.put(no_raiz)

    while not fila.empty():
        
        it = it +1
        no = fila.get()
        
        for sucessor in no.get_sucessores():
            if sucessor == objetivo:
                return {'node': sucessor, 'stored': fila.qsize(), 'iterations': it, 'time': dt.datetime.now() - ini}
            fila.put(sucessor)
        # print(fila.queue)
        # return False

    return None
