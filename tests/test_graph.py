import unittest
from graph import Graph
import random
from itertools import product


class GraphTest(unittest.TestCase):
    def testbfs(self):
        num_v = 10
        vertices = list(range(0, num_v))
        edges = random.sample(list(product(vertices, vertices)), 5*num_v)
        g = Graph(vertices, edges)
        vert_order = g.bfs()
        self.assertLessEqual(len(vert_order),len(vertices))


if __name__ == '__main__':
    unittest.main()