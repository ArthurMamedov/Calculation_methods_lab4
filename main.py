from modules import *

if __name__ == '__main__':
    print('Enter the expanded matrix:')
    matrix = ask_for_matrix()
    matrix2 = [list(row) for row in matrix]
    print(f'Roots (got using Gauss): {Gauss(matrix)}')
    print('Roots (got using Seidel): {}, iterations: {}'.format(*Seidel(matrix2, 0.0001)))
