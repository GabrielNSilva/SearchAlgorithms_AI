from copy import deepcopy

class Node:

    def __init__(self, state, parent=None, deepth=0, cost=0, action=None, heuristica=0):
        self.state  = state
        self.parent = parent
        self.deepth = deepth
        self.cost   = cost
        self.action = action
        self.heuristica = heuristica

    def __eq__(self, node):
        return (self.state == node.state)

    def __str__(self):
        return '\n\t Deepth: ' + str(self.deepth) + '\n\t Cost: ' + str(self.cost) + '\n\t State:\n' + str(self.state)
        
    def path(self):
        parent_path = self.parent.path() if self.parent else ''
        return parent_path  + '\n\t Deepth: ' + str(self.deepth) + '\n\t Cost: ' + str(self.cost) + '\n\t State:\n' + str(self.state)
            
    def get_sucessores(self):
        children = list()
        for m in range(4):
            state_aux = deepcopy(self.state)
            if state_aux.move(m):
                node_aux = Node(state_aux, self, self.deepth+1, self.cost+1)
                children.append(node_aux)
        return children