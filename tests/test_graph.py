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

    def testavg_degree(self):
        num_v = 10
        connectivity = 3
        prob_correct = []


        for i in range(100):
            vertices = list(range(0, num_v))
            edges = []
            # reservoir sampling to construct edge list because loading product
            # is too memory intensive
            for i,e in enumerate(product(vertices, vertices)):
                if i < connectivity*num_v:
                    edges.append(e)
                else:
                    j = random.randint(0,i)
                    if j < connectivity*num_v:
                        edges[j] = e
            # edges = random.sample(product(vertices, vertices), connectivity*num_v)
            # enforce minimum degree 1
            for i in range(num_v):
                edges.append((i, random.choice(range(num_v))))
            g = Graph(vertices, edges)
            err = .4
            est = g.avg_deg(err, 1)

            prob_correct.append((1-err)*(connectivity+1) <= est <= (1+err)*(connectivity+1))
        # print(sum(map(int,prob_correct))/len(prob_correct))
        self.assertGreaterEqual(sum(map(int,prob_correct))/len(prob_correct),.6)


if __name__ == '__main__':
    unittest.main()