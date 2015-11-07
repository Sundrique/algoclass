import random


def GetRandomEdge(edges):
    return edges[random.choice(edges.keys())]


def Contract(edges, vertices, contractedEdge):
    u = contractedEdge.u
    v = contractedEdge.v

    for key, edge in enumerate(v.adjacent):
        if edge.u == v:
            edge.u = u
        elif edge.v == v:
            edge.v = u
        u.adjacent.append(edge)

    vertices.pop(v.label, None)

    adjacent = u.adjacent
    u.adjacent = []
    for key, edge in enumerate(adjacent):
        if edge.u == edge.v:
            if hash(edge) in edges:
                del edges[hash(edge)]
        else:
            u.adjacent.append(edge)


def MinCut(edges, vertices):

    prev = len(vertices)
    while len(vertices) > 2:
        randomEdge = GetRandomEdge(edges)
        Contract(edges, vertices, randomEdge)
        if len(vertices) == prev:
            return len(edges)
        else:
            prev = len(vertices)


    return len(edges)


class Edge(object):
    def __init__(self, u, v):
        self.u = u
        self.v = v
        u.adjacent.append(self)
        v.adjacent.append(self)

    def __repr__(self):
        return '(' + str(self.u) + ', ' + str(self.v) + ')'


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.adjacent = []

    def __repr__(self):
        return str(self.label)


def ProcessLines(lines):
    vertices = {}
    edges = {}
    for line in lines:
        labels = line.rstrip().split('\t')
        vertices[labels[0]] = Vertex(labels[0])
        for label in labels[1:]:
            if label in vertices:
                edge = Edge(vertices[labels[0]], vertices[label])
                edges[hash(edge)] = edge

    return vertices, edges

if __name__ == '__main__':
    fileName = 'kargerMinCut.txt'
    lines = []
    for line in open(fileName):
        lines.append(line)

    n = len(lines)
    minCut = n - 1
    iterations = n

    for i in range(0, iterations):
        vertices, edges = ProcessLines(lines)
        minCut = min(minCut, MinCut(edges, vertices))

    print minCut
