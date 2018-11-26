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
    print(response)

    print('\t\t Custo de Busca')
    print(' d | Gulosa (h1) | Gulosa (h2) | A* (h1) | A* (h2) |')
    for i in range(7):
        print(' {0:1d} | {1:5.3f} | {2:5.3f} | {3:5.3f} | {4:5.3f} |'.format(
            i+2,
            response['gu_h1'][i]['max_stored'],
            response['gu_h2'][i]['max_stored'],
            response['ae_h1'][i]['max_stored'],
            response['ae_h2'][i]['max_stored']))
