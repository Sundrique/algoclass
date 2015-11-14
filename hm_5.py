import heapq
import re


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.adjacent = {}

    def __repr__(self):
        return str(self.label) + ' adjacent:' + str(self.adjacent)


def GetNode(label, vertices):
    if label not in vertices:
        vertices[label] = Vertex(label)
    return vertices[label]


def BuildGraph(fileName):
    vertices = {}
    for line in open(fileName):
        nodes = re.compile("\s").split(line.rstrip())

        node = GetNode(nodes[0], vertices)

        for adjacent in nodes[1:]:
            label, weight = adjacent.split(',')
            weight = int(weight)
            adjNode = GetNode(label, vertices)
            node.adjacent[int(label)] = int(weight)
            adjNode.adjacent[node.label] = int(weight)

    return vertices


def BuildHeap(vertices, start='1'):
    h = []
    for label in vertices:
        dist = 1000000
        if label == start:
            dist = 0
        heapq.heappush(h, (dist, label))

    return h


def Min(h, vertices):
    minWeight, minLabel = heapq.heappop(h)

    tmp = []
    while len(h) > 0:
        weight, label = heapq.heappop(h)
        vertex = vertices[label]
        if minLabel in vertex.adjacent:
            weight = min(weight, minWeight + vertex.adjacent[minLabel])
        tmp.append((weight, label))

    for v in tmp:
        heapq.heappush(h, v)

    return minLabel, minWeight


if __name__ == '__main__':
    vertices = BuildGraph('dijkstraData.txt')
    h = BuildHeap(vertices)
    A = {}
    while len(h) > 0:
        minLabel, minWeight = Min(h, vertices)
        A[minLabel] = minWeight

    keys = ['7', '37', '59', '82', '99', '115', '133', '165', '188', '197']
    print ','.join([str(A[k]) for k in keys])