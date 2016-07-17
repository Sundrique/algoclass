file_name = 'clustering1.txt'

node_to_cluster = {}
cluster_to_nodes = {}
number_of_clusters = 0


def get_data(file_name):
    distances = []
    global number_of_clusters
    with open(file_name) as f:
        for i, line in enumerate(f):
            if i == 0:
                n = int(line)
            else:
                node1, node2, distance = map(int, line.strip().split(' '))
                distances.append((distance, (node1, node2)))

    node_to_cluster = {i: i for i in range(1, n + 1)}
    cluster_to_nodes = {i: {i} for i in range(1, n + 1)}
    number_of_clusters = n
    return n, node_to_cluster, cluster_to_nodes, distances


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


if __name__ == '__main__':
    n, node_to_cluster, cluster_to_nodes, distances = get_data(file_name)
    print(max_spacing(distances, 4))
