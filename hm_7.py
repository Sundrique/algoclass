import heapq

file_name = 'jobs.txt'

edges_file_name = 'edges.txt'


def get_data(file_name):
    jobs = []
    with open(file_name) as f:
        for i, line in enumerate(f):
            if i == 0:
                n = int(line)
            else:
                jobs.append(tuple(map(int, line.strip().split(' '))))

    return n, jobs


def get_weighted_sum(jobs, ordering=lambda job: (job[1] - job[0], -job[0])):
    completion_time = 0
    sum = 0
    for job in sorted(jobs, key=ordering):
        completion_time += job[1]
        sum += completion_time * job[0]
    return sum


poped = {}
def edges_sum(vertices, edges):
    sum = 0
    while len(vertices) > 0:
        cost, vertex = heapq.heappop(vertices)
        if vertex is not REMOVED and vertex not in poped:
            poped[vertex] = True
            sum += cost
            for (v, w) in edges[vertex]:
                if v not in poped:
                    update(vertices, v, w)

    return sum


def construct_graph(file_name):
    with open(file_name) as f:
        for i, line in enumerate(f):
            if i == 0:
                nv, ne = tuple(map(int, line.strip().split(' ')))
                edges = {j + 1: set() for j in range(nv)}
            else:
                fr, to, w = tuple(map(int, line.strip().split(' ')))
                edges[fr] |= {(to, w)}
                edges[to] |= {(fr, w)}

    vertices = []
    for j in range(nv):
        vertex = [9223372036854775807, j + 1]
        entry_finder[j + 1] = vertex
        vertices.append(vertex)

    vertices[0][0] = 0

    return vertices, edges


entry_finder = {}
REMOVED = -1

def update(vertices, node, cost):
    entry = entry_finder[node]
    if entry[0] > cost:
        entry[-1] = REMOVED

        vertex = [cost, node]
        heapq.heappush(vertices, vertex)
        entry_finder[node] = vertex


if __name__ == '__main__':
    _, jobs = get_data(file_name)
    print(get_weighted_sum(jobs))
    ordering = lambda job: - 1.0 * job[0] / job[1]
    print(get_weighted_sum(jobs, ordering=ordering))

    vertices, edges = construct_graph(edges_file_name)
    print(edges_sum(vertices, edges))
