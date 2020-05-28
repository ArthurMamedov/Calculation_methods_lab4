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


def Seidel(matrix: 'matrix', e: 'error'):
    n = len(matrix)
    x, i = [1] * n, 0
    while True:
        R = 0
        for i in range(0, n):
            S = 0
            for j in range(0, n):
                if j != i:
                    S += matrix[i][j] * x[j]
            W = (matrix[i][n] - S) / matrix[i][i]
            d = abs(W - x[i])
            R = d if R < d else R
            x[i] = W
        if R <= e:
            return x, i
        else:
            i += 1
