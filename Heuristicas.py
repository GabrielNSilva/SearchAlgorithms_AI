def h1(no, objetivo):
    h = 0
    hl = list()
    for col in range(len(no.state.matrix)):
        for row in range(len(no.state.matrix[col])):
            if no.state.matrix[row][col] != objetivo.state.matrix[row][col] and no.state.matrix[row][col] != None:
                h += 1
                hl.append(no.state.matrix[row][col])
    return h


def pos(x, mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == x:
                return (i, j)

def h2(no, objetivo):
    h = 0
    hl = list()
    for row in range(len(no.state.matrix)):
        for col in range(len(no.state.matrix[row])):
            if no.state.matrix[row][col] != None:
                pos_obj = pos(no.state.matrix[row][col], objetivo.state.matrix)
                pos_atual = (row, col)
                hl.append(abs(pos_obj[0]-pos_atual[0]) + abs(pos_obj[1]-pos_atual[1]))
                h += hl[-1]
    return h
