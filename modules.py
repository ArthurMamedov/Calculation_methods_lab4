from colorama import Fore as fr, init
init()

if __name__ == '_-main__':
    print('Error: Program shall be run from "main.py" file.')
    exit()


def str_to_tuple(string: str):
    try:
        tpl = [float(x) for x in string.split(' ')]
        return tpl
    except ValueError:
        return None


def ask_for_matrix():
    size, matrix = None, list()
    while True:  #matrix filling
        ls = str_to_tuple(input())
        if size is None:
            size = len(ls) - 1
        if ls is not None and len(ls) - 1 == size:
            matrix.append(ls)
        else:
            print(f'{fr.LIGHTRED_EX}Bad input error!{fr.LIGHTRED_EX}')
            exit()
        if size == len(matrix):
            return matrix


def Gauss(matrix: 'matrix'):
    size = len(matrix)
    answers = [0] * size
    for k in range(1, size):
        for j in range(k, size):
            m = matrix[j][k-1] / matrix[k-1][k-1]
            for i in range(size + 1):
                matrix[j][i] -= m * matrix[k-1][i]

    for i in range(size-1, -1, -1):
        answers[i] = matrix[i][size] / matrix[i][i]
        for c in range(size-1, i, -1):
            answers[i] -= matrix[i][c] * answers[c] / matrix[i][i]
    return answers


def Seidel(matrix, e):
    size = len(matrix)
    matrix2 = [[0] * size] * size
    for f in range(size):
        matrix2[f] = [-x for x in matrix[f][0:-1]]
        matrix2[f][f] = matrix[f][size]
        for ff in range(size):
            matrix2[f][ff] /= matrix[f][f]
    matrix = matrix2
    Xs, lXs, it = [0] * size, [0] * size, 0
    while True:
        it += 1
        for c in range(size):
            Xs[c] = matrix[c][c]
            for p in range(size):
                if c != p:
                    Xs[c] += matrix[c][p] * Xs[p]
        _e = abs(Xs[0] - lXs[0])
        for c in range(1, size):
            if abs(Xs[c] - lXs[c] > _e):
                _e = abs(Xs[c] - lXs[c])
        if e > _e:
            return Xs, it
        lXs = list(Xs)




if __name__ == '__main__':
    matrix = [[1,2,3,0], [4,5,6,0], [7,8,9,0]]
    Seidel(matrix, 0.0001)