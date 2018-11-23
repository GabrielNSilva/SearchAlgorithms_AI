import numpy as np

class Puzzle():
    
    def __init__(self, width, heigth, matrix = None):
        self.width  = width
        self.heigth = heigth
        if matrix == None:
            self.matrix = self.generate()
        else:
            self.matrix = np.array(matrix) if not isinstance(matrix, np.ndarray) else matrix
        self.empty  = None if None in self.matrix else 0

    def __str__(self):
        string = '\t '
        for row in self.matrix:
            # string = string + ' '.join(map(str, row)) + '\n'
            for col in row:
                # col = '\u2400' if col == None else col
                col = '-' if col == None else col
                string = string + str(col) + '\t'
            string = string + '\n\t '
        return string

    def __eq__(self, p):
        return (self.matrix == p.matrix).all()

    def get_empty_pos(self): # busca a posicao vazia e retorna um dict ou False
        if None in self.matrix or 0 in self.matrix:
            pos = np.concatenate(np.where(self.matrix == self.empty))
            return {'x':pos[0], 'y':pos[1]}
        else:
            return False

    def pos_is_valid(self, pos):
        return pos['x'] >= 0 and pos['y'] >= 0 and \
                pos['x'] < self.heigth and pos['y'] < self.width

    def move_possible(self, m):
        if   m == 0: m = {'x':0, 'y':1}  # move vazio para a direita
        elif m == 1: m = {'x':0, 'y':-1} # move vazio para a esquerda
        elif m == 2: m = {'x':1, 'y':0}  # move vazio para baixo
        elif m == 3: m = {'x':-1, 'y':0} # move vazio para cima

        ep = self.get_empty_pos()
        if not ep: return False, False

        pos = {'x': ep['x']+m['x'], 'y': ep['y']+m['y']}
        if not self.pos_is_valid(pos): return False, False

        return ep, pos

    def move(self, m):
        ep, pos = self.move_possible(m)
        if not ep: return False

        self.matrix[ep['x']][ep['y']]   = self.matrix[pos['x']][pos['y']]
        self.matrix[pos['x']][pos['y']] = self.empty
        return True