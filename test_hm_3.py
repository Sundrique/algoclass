import unittest
import hm_3

class TestStringMethods(unittest.TestCase):
    def test_ProcessRow(self):
        lines = ["1 2 3\r\n", "2 3 1\r\n", "3 1 2\r\n"]
        vertices, edges = hm_3.ProcessLines(lines)
        self.assertEqual(len(vertices), 3)
        self.assertEqual(len(edges), 3)

        lines = ["1 2 3 4 7\r\n", "2 1 3 4\r\n", "3 1 2 4\r\n", "4 1 2 3 5\r\n", "5 4 6 7 8\r\n", "6 5 7 8\r\n",
                 "7 1 5 6 8\r\n", "8 5 6 7\r\n"]
        vertices, edges = hm_3.ProcessLines(lines)
        self.assertEqual(len(vertices), 8)
        self.assertEqual(len(edges), 14)

    def test_Contract(self):
        vertices = {'1': hm_3.Vertex('1'), '3': hm_3.Vertex('3'), '2': hm_3.Vertex('2'), '5': hm_3.Vertex('5'),
                    '4': hm_3.Vertex('4'), '7': hm_3.Vertex('7'), '6': hm_3.Vertex('6'), '8': hm_3.Vertex('8')}

        edges = [hm_3.Edge(vertices['2'], vertices['1']), hm_3.Edge(vertices['3'], vertices['1']),
                 hm_3.Edge(vertices['3'], vertices['2']), hm_3.Edge(vertices['4'], vertices['1']),
                 hm_3.Edge(vertices['4'], vertices['2']), hm_3.Edge(vertices['4'], vertices['3']),
                 hm_3.Edge(vertices['5'], vertices['4']), hm_3.Edge(vertices['6'], vertices['5']),
                 hm_3.Edge(vertices['7'], vertices['1']), hm_3.Edge(vertices['7'], vertices['5']),
                 hm_3.Edge(vertices['7'], vertices['6']), hm_3.Edge(vertices['8'], vertices['5']),
                 hm_3.Edge(vertices['8'], vertices['6']), hm_3.Edge(vertices['8'], vertices['7'])]

        edgesMap = {}
        for edge in edges:
            edgesMap[hash(edge)] = edge

        hm_3.Contract(edgesMap, vertices, edgesMap[hash(edges[2])])

        self.assertEqual(len(vertices['3'].adjacent), 4)
        self.assertEqual(len(vertices), 7)
        self.assertEqual(len(edgesMap), 13)

        hm_3.Contract(edgesMap, vertices, edgesMap[hash(edges[0])])

        self.assertEqual(len(vertices['3'].adjacent), 4)
        self.assertEqual(len(vertices), 6)
        self.assertEqual(len(edgesMap), 11)

    def test_MinCut(self):
        vertices = {'1': hm_3.Vertex('1'), '3': hm_3.Vertex('3'), '2': hm_3.Vertex('2'), '5': hm_3.Vertex('5'),
                    '4': hm_3.Vertex('4'), '7': hm_3.Vertex('7'), '6': hm_3.Vertex('6'), '8': hm_3.Vertex('8')}
        edges = [hm_3.Edge(vertices['2'], vertices['1']), hm_3.Edge(vertices['3'], vertices['1']),
                 hm_3.Edge(vertices['3'], vertices['2']), hm_3.Edge(vertices['4'], vertices['1']),
                 hm_3.Edge(vertices['4'], vertices['2']), hm_3.Edge(vertices['4'], vertices['3']),
                 hm_3.Edge(vertices['5'], vertices['4']), hm_3.Edge(vertices['6'], vertices['5']),
                 hm_3.Edge(vertices['7'], vertices['1']), hm_3.Edge(vertices['7'], vertices['5']),
                 hm_3.Edge(vertices['7'], vertices['6']), hm_3.Edge(vertices['8'], vertices['5']),
                 hm_3.Edge(vertices['8'], vertices['6']), hm_3.Edge(vertices['8'], vertices['7'])]

        edgesMap = {}
        for edge in edges:
            edgesMap[hash(edge)] = edge

        hm_3.MinCut(edgesMap, vertices)

        self.assertEqual(len(vertices), 2)

if __name__ == '__main__':
    unittest.main()