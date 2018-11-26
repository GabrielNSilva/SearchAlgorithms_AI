from random import randint
from time import sleep
from copy import deepcopy
import datetime as dt

PRINT_ATIVO = True
PRINT_ATIVO = False

def printif(string=''):
    if PRINT_ATIVO:
        print(string)


def print_reponse(response):

    if response['success']:
        print('\t- Iterações: ' + str(response['iterations']))
        print('\t- Tempo: ' + str(response['time']))
        print('\t- Nodes armazenados (memória) [max]: ' + str(response['max_stored']))
        print('\t- Nodes armazenados (memória) [fim]: ' + str(response['stored']))
        print('\t- Node resposta: ' + str(response['node']))
        # print('\t- Caminho: ' + response['node'].path())
    else:
        print('Falhou!')
        print('\t- Iterações: ' + str(response['iterations']))
        print('\t- Tempo: ' + str(response['time']))
        print('\t- Nodes armazenados (memória) [max]: ' + str(response['max_stored']))
        print('\t- Nodes armazenados (memória) [fim]: ' + str(response['stored']))

    print()
    print('-------------------------------------------------------')
    print()


def print_avg(response):

    print('\tMÉDIAS:')
    print('\t- Iterações: ' + str(response['iterations']))
    print('\t- Tempo: ' + str(response['time']))
    print('\t- Nodes armazenados (memória) [max]: ' + str(response['max_stored']))
    print('\t- Nodes armazenados (memória) [fim]: ' + str(response['stored']))


def print_avg_table(response):
    printif(response)
    for i in range(7):
        printif('[\'gu_h1\']['+str(i)+'] = '+str(response['gu_h1'][i]))
        printif('[\'gu_h2\']['+str(i)+'] = '+str(response['gu_h2'][i]))
        printif('[\'ae_h1\']['+str(i)+'] = '+str(response['ae_h1'][i]))
        printif('[\'ae_h2\']['+str(i)+'] = '+str(response['ae_h2'][i]))

    print('-------------------Custo de Busca--------------------')
    print('| d | Gulosa (h1) | Gulosa (h2) | A* (h1) | A* (h2) |')
    for i in range(7):
        print('| {0:1d} |    {1:5.1f}    |    {2:5.1f}    |  {3:5.1f}  |  {4:5.1f}  |'.format(
            i+2,
            response['gu_h1'][i]['max_stored'],
            response['gu_h2'][i]['max_stored'],
            response['ae_h1'][i]['max_stored'],
            response['ae_h2'][i]['max_stored']))

    print('------------Fator de Ramificação Efetivo-------------')
    print('| d | Gulosa (h1) | Gulosa (h2) | A* (h1) | A* (h2) |')
    for i in range(7):
        # Cálculo do fator de ramificacao (b*)
        response['gu_h1'][i]['b*'] = fator_ramificacao(response['gu_h1'][i]['max_stored'], i+2)
        response['gu_h2'][i]['b*'] = fator_ramificacao(response['gu_h2'][i]['max_stored'], i+2)
        response['ae_h1'][i]['b*'] = fator_ramificacao(response['ae_h1'][i]['max_stored'], i+2)
        response['ae_h2'][i]['b*'] = fator_ramificacao(response['ae_h2'][i]['max_stored'], i+2)

        print('| {0:1d} |    {1:5.3f}    |    {2:5.3f}    |  {3:5.3f}  |  {4:5.3f}  |'.format(
            i+2,
            response['gu_h1'][i]['b*'],
            response['gu_h2'][i]['b*'],
            response['ae_h1'][i]['b*'],
            response['ae_h2'][i]['b*']))
    print('-----------------------------------------------------')

def fator_ramificacao(N, d):
    printif('*********************************************** fator_ramificacao('+str(N)+', '+str(d)+')')
    hv = 10
    mv = 0
    b = (hv+mv)/2
    printif('hv'+str(hv)+' mv'+str(mv)+' -> b'+str(b))
    nbd = n(b, d)
    printif(str(N)+'-'+str(nbd)+'='+str(N - nbd))
    while abs(N - nbd) > 0.001:
        if N < nbd:
            hv = b
        else:
            mv = b
        b = (hv+mv)/2
        printif('hv '+str(hv)+'  mv '+str(mv)+'  -> b '+str(b))
        nbd = n(b, d)
        printif(str(N)+' - '+str(nbd)+' = '+str(N - nbd))
        # sleep(0.5)
    return b

def n(b, d):
    x = 0
    for de in range(d):
        x += b**de
    return x
