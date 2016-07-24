from decimal import *

file_name = 'g0.txt'


def get_data(file_name):
    infinity = Decimal('Infinity')

    with open(file_name) as f:
        for i, line in enumerate(f):
            if i == 0:
                n, _ = map(int, line.strip().split(' '))
                base_case = [[infinity for _ in range(n)] for _ in range(n)]
                for j in range(n):
                    base_case[j][j] = 0
            else:
                head, tail, length = map(int, line.strip().split(' '))
                base_case[head - 1][tail - 1] = length

    table = base_case
    return n, table


def get_min(n, base_case):
    previous = base_case
    negative = False
    shortest = Decimal('Infinity')
    for k in range(n):
        new = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new[i][j] = min(previous[i][j], previous[i][k - 1] + previous[k - 1][j])
                shortest = min(new[i][j], shortest)
                if i == j and new[i][j] < 0:
                    negative = True
        previous = new

    return new, shortest, negative


if __name__ == '__main__':
    for file_name in ['g1.txt', 'g2.txt', 'g3.txt']:
        n, base_case = get_data(file_name)
        _, shortest, negative = get_min(n, base_case)

        print(shortest)
        if negative:
            print('Negative cycle')
        print('------------')
