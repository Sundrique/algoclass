import sys


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.out = []
        self.revOut = []
        self.visited = False
        self.revVisited = False
        self.next = None

    def __repr__(self):
        return str(self.label)


listHead = None


def RevDFS(node):
    global listHead
    node.revVisited = True

    for label in node.revOut:
        if not vertices[label].revVisited:
            RevDFS(vertices[label])

    if listHead is not None:
        node.next = listHead

    listHead = node


def DFS(node):
    global i, SCCs
    node.visited = True

    SCCs[i] += 1

    for label in node.out:
        if not vertices[label].visited:
            DFS(vertices[label])


def DFSIterative(node):
    global i, SCCs

    stack = [node]

    while len(stack) > 0:
        n = stack.pop()
        if not n.visited:
            n.visited = True
            SCCs[i] += 1

            for label in n.out:
                o = vertices[label]
                stack.append(o)


def BuildGraph(fileName):
    vertices = {}
    for line in open(fileName):
        tailLabel, headLabel = line.rstrip().split(' ')

        if tailLabel in vertices:
            tail = vertices[tailLabel]
        else:
            tail = Vertex(tailLabel)
            vertices[tailLabel] = tail

        if headLabel in vertices:
            head = vertices[headLabel]
        else:
            head = Vertex(headLabel)
            vertices[headLabel] = head

        tail.out.append(headLabel)
        head.revOut.append(tailLabel)

    return vertices


if __name__ == '__main__':
    sys.setrecursionlimit(70000)

    vertices = BuildGraph('SCC.txt')

    for label in vertices:
        node = vertices[label]
        if not node.revVisited:
            RevDFS(node)

    node = listHead
    i = 0
    SCCs = [0]
    while True:
        if not node.visited:
            DFSIterative(node)
            i += 1
            SCCs.append(0)
        if node.next is None:
            break
        node = node.next

    print(sorted(SCCs, reverse=True)[:10])
