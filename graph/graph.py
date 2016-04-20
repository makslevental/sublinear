from collections import deque, Counter
from math import ceil, log, sqrt
import random
from intervaltree import IntervalTree

class GraphError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Vertex(object):
    def __init__(self, name: str, value=None, children: list=None, parent: 'Vertex'=None) -> None:
        if name is not None:
            self.name = name
        else:
            raise GraphError("Vertex must be named")

        self.value = value
        self.children = children if children is not None else []

        self.visited = False
        self.distance = 0
        self.parent = parent

    def __str__(self):
        if self.value is not None:
            return repr(self.value)
        else:
            return self.name

    def set(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self

    def deg(self):
        return len(self.children)


class Graph(object):
    def __init__(self, vertices: list, edges: [tuple]) -> None:
        self.vertices = len(vertices)*[None]
        for i, v in enumerate(vertices):
            self.vertices[i] = Vertex(name=str(v))
        # edges are directed. undirected graphs will be represented by double edges
        self.edges = edges
        for e in self.edges:
            self.vertices[e[0]].children.append(self.vertices[e[1]])

    def bfs(self, root: Vertex=None):
        ptr = root if root is not None else self.vertices[0]

        vert_order = []
        ptr.distance = 0
        que = deque([ptr])

        while que:
            ptr = que.popleft()
            if ptr.visited:
                continue
            else:
                vert_order.append(ptr)
                ptr.visited = True
                que.extend([v.set(parent=ptr, distance=ptr.distance+1)
                          for v in ptr.children if v.visited is not True])
        return vert_order

    def avg_deg(self, err: float, l_bound: int) -> float:
        beta = err/8
        num_v = len(self.vertices)
        samp_sz = ceil( (sqrt(num_v/l_bound)) * (err**(-4.5)) * ((log(num_v))**2) * (log(1/err)) )
        samp = Counter()
        for i in range(samp_sz):
            samp[random.choice(self.vertices)] += 1

        num_b = ceil(log(num_v,1+beta))+1
        samp_i = num_b*[None]
        for i in range(num_b):
            samp_i[i] = [((v,count), ((1+beta)**(i-1),(1+beta)**i)) for v,count in samp.items()
                         if (1+beta)**(i-1) < v.deg() <= (1+beta)**i]

        lg_bins = list(filter(lambda s: sum([ss[0][1] for ss in s])/samp_sz >= (1/num_b)*sqrt((err/6)*(l_bound/num_v)), samp_i))

        sml_bins = IntervalTree.from_tuples([bin[0][1] for bin in lg_bins])


        alpha_i = []
        for b in lg_bins:
            alpha = 0
            for (v,count),_ in b:
                for i in range(count):
                    nei = random.choice(v.children)
                    # if nei is not in a large bin then xi(v) = 1, ie if nei is in a "small" bucket
                    if len(sml_bins.search(nei.deg())) == 0:
                        alpha += 1
                    # if nei is in a large bin then xi(v) = 0
            alpha_i.append(alpha/sum([count for (_, count), _ in b]))

        return (1/samp_sz)*sum([(1+alpha_i[i])*sum([count for (_, count), _ in lg_bins[i]])*lg_bins[i][0][1][1] for i in range(len(lg_bins))])

