PRINT_ATIVO = True
# PRINT_ATIVO = False

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
        print('\t- Caminho: ' + response['node'].path())
    else:
        print('Falhou!')
        print('\t- Iterações: ' + str(response['iterations']))
        print('\t- Tempo: ' + str(response['time']))
        print('\t- Nodes armazenados (memória) [max]: ' + str(response['max_stored']))
        print('\t- Nodes armazenados (memória) [fim]: ' + str(response['stored']))

    print()
    print('-------------------------------------------------------')
    print()
