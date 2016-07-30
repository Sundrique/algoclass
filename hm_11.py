import itertools
import math
import time
from itertools import combinations


def dist(a, b):
    return math.sqrt(math.pow(cities[a][0] - cities[b][0], 2) + math.pow(cities[a][1] - cities[b][1], 2))


def length(x, y):
    return math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2))


def solve_tsp_dynamic(points):
    # calc all lengths
    all_distances = [[length(x, y) for y in points] for x in points]
    # initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx + 1]), idx + 1): (dist, [0, idx + 1]) for idx, dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min([(A[(S - {j}, k)][0] + all_distances[k][j], A[(S - {j}, k)][1] + [j]) for k in S if
                                 k != 0 and k != j])  # this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res[1]


def get_data(file_name):
    cities = []

    with open(file_name) as f:
        for i, line in enumerate(f):
            if i != 0:
                x, y = map(float, line.strip().split(' '))
                cities.append((x, y))

    return cities


if __name__ == '__main__':

    file_name = 'tsp.txt'

    cities = get_data(file_name)
    n = len(cities)

    full_set = frozenset(range(1, n))
    combs = [() for _ in range(n)]
    for i in range(2, n):
        combs[i] = combinations(full_set, i)

    start_time = time.time()

    dists = {}
    for i in range(n):
        for j in range(n):
            dists[(i, j)] = dist(i, j)

    results = {}
    for i in range(1, n):
        key = (i, frozenset([i]))
        results[key] = dists[(0, i)]

    for i in range(2, n):
        print("M =", i)
        for c in combs[i]:
            S = frozenset(c)
            for j in S:
                S_j = S - {j}
                m = float('inf')
                for k in S_j:
                    m = min(m, results[(k, S_j)] + dists[(k, j)])

                results[(j, S)] = m

    m = float('inf')
    for i in full_set:
        m = min(m, results[(i, full_set)] + dists[(0, i)])

    # p = solve_tsp_dynamic(cities)
    # m = 0
    # for i,_ in enumerate(p[:-1]):
    #     m += dist(p[i], p[i+1])
    #
    # m += dist(p[-1], p[0])

    print(m)
    print("--- %s seconds ---" % (time.time() - start_time))
