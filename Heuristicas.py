def h1(no, objetivo):
    h = 0
    for col in range(len(no.state.matrix)):
        for row in range(len(no.state.matrix[col])):
            if no.state.matrix[row][col] != objetivo.state.matrix[row][col]:
                h += 1
    return h


def h2(no, objetivo):
    h = 0
    for col in range(len(no.state.matrix)):
        for row in range(len(no.state.matrix[col])):
            