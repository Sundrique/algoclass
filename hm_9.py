def get_data(file_name):
    items = []
    global number_of_clusters
    with open(file_name) as f:
        for i, line in enumerate(f):
            if i == 0:
                W, _ = map(int, line.strip().split(' '))
            else:
                v, w = map(int, line.strip().split(' '))
                items.append((v, w))

    return W, items


if __name__ == '__main__':
    file_name = 'knapsack1.txt'
    W, items = get_data(file_name)
    n = len(items)
    table = [[0 for _ in range(n + 1)] for _ in range(W + 1)]
    for i in range(1, W + 1):
        for j in range(1, n + 1):
            v, w = items[j - 1]
            using = (v + table[i - w][j - 1]) if w <= i else 0
            not_using = table[i][j - 1]
            table[i][j] = max(using, not_using)

    print(table[W][n])
