from __future__ import division
import unittest
from graph import Graph
import random
from itertools import product
import gzip
from math import ceil,sqrt

class GraphTest(unittest.TestCase):
    def testbfs(self):
        num_v = 10
        vertices = list(range(0, num_v))
        edges = random.sample(list(product(vertices, vertices)), 5*num_v)
        g = Graph(vertices, edges)
        vert_order = g.bfs()
        self.assertLessEqual(len(vert_order),len(vertices))

    def testavg_degree(self):
        num_v = 1632803+1
        # connectivity = random.randint(10,int(ceil(sqrt(num_v))))
        prob_correct = []

        with gzip.open('/home/maksim/Downloads/soc-pokec-relationships.txt.gz','rt') as f:

            for i in range(100):
                vertices = list(range(0, num_v))
                edges = []
                # reservoir sampling to construct edge list because loading product
                # is too memory intensive
                for line in f:
                   edge = line.split()
                   edges.append((int(edge[0]), int(edge[1])))
                # edges = random.sample(product(vertices, vertices), connectivity*num_v)
                # enforce minimum degree 1
                for i in range(num_v):
                       edges.append((i, random.choice(range(num_v))))
                g = Graph(vertices, edges)
                err = .4
                est = g.avg_deg(err, 1)

            connectivity = sum(v.deg() for v in g.vertices)/num_v
            prob_correct.append((1-err)*(connectivity+1) <= est <= (1+err)*(connectivity+1))
        print sum(map(int,prob_correct))/len(prob_correct)
        self.assertGreaterEqual(sum(map(int,prob_correct))/len(prob_correct),.6)



if __name__ == '__main__':
    unittest.main()