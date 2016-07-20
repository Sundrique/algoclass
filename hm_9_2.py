import sys

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

memo = {}
def knapsack(items, W):

    key = (len(items), W)
    if key not in memo:
        if len(items) == 0 or W <= 0:
            memo[key] = 0
        else:
            v, w = items[-1]
            if w > W:
                memo[key] = knapsack(items[:-1], W)
            else:
                memo[key] = max(
                        knapsack(items[:-1], W),
                        knapsack(items[:-1], W - w) + v
                )

    return memo[key]

if __name__ == '__main__':
    file_name = 'knapsack_big.txt'
    W, items = get_data(file_name)
    sys.setrecursionlimit(10000)
    print(knapsack(items, W))
