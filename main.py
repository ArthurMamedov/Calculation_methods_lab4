from modules import *

if __name__ == '__main__':
    print('Enter the expanded matrix:')
    matrix = ask_for_matrix()

    print(f'Roots (got using Gauss): {Gauss(list(matrix))}')
    print('Roots (got using Seidel): {}, iterations: {}'.format(*Seidel(list(matrix), 0.0001)))
