file_name = 'clustering_big.txt'

node_to_cluster = {}
cluster_to_nodes = {}
number_of_clusters = 0


def bits_to_int(bits):
    out = 0
    for bit in bits:
        out = (out << 1) | bit
    return out

def get_data(file_name):
    global number_of_clusters

    with open(file_name) as f:
        for i, line in enumerate(f):
            if i == 0:
                n, nbits = map(int, line.strip().split(' '))
            else:
                bits = map(int, line.strip().split())
                num = bits_to_int(bits)
                if num not in node_to_cluster:
                    node_to_cluster[num] = num
                    cluster_to_nodes[num] = {num}
                    number_of_clusters += 1

    return n, nbits, node_to_cluster, cluster_to_nodes


def find(node):
    return node_to_cluster[node]


def union(a, b):
    global number_of_clusters

    if len(cluster_to_nodes[a]) < len(cluster_to_nodes[b]):
        a, b = b, a
    for node in cluster_to_nodes[b]:
        node_to_cluster[node] = a

    cluster_to_nodes[a] |= cluster_to_nodes[b]
    del cluster_to_nodes[b]
    number_of_clusters -= 1


def max_spacing(distances, k):
    for dist, (node1, node2) in sorted(distances):
        if find(node1) != find(node2):
            union(find(node1), find(node2))
        if number_of_clusters < k:
            return dist


def get_one_diff(num, bits=24):
    for i in range(bits):
        yield num ^ (1 << i)


def get_two_diff(num, bits=24):
    for i, one_diff in enumerate(get_one_diff(num)):
        for j in range(bits):
            if j != i:
                yield one_diff ^ (1 << j)

def greater_one(num, bits=24):
    for one_diff in get_one_diff(num, bits):
        if one_diff > num:
            yield one_diff

def greater_two(num, bits=24):
    for two_diff in get_two_diff(num, bits):
        if two_diff > num:
            yield two_diff


if __name__ == '__main__':
    n, bits, node_to_cluster, cluster_to_nodes = get_data(file_name)

    print(number_of_clusters)

    for node1 in sorted(node_to_cluster):
        for node2 in greater_one(node1, bits):
            if node2 in node_to_cluster:
                if find(node1) != find(node2):
                    union(find(node1), find(node2))

    for node1 in sorted(node_to_cluster):
        for node2 in greater_two(node1, bits):
            if node2 in node_to_cluster:
                if find(node1) != find(node2):
                    union(find(node1), find(node2))

    print(number_of_clusters)
