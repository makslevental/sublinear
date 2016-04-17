from itertools import product
import random
from collections import deque

class Vertex():
    def __init__(self,name:str,value=None,children:list=None):
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        else:
            self.value = None

        if children is not None:
            self.children = children
        else:
            self.children = []
            # maybe cache misses will be bad?
            # Q is long long 8 bytes
            # self.children = array('Q')

        self.visited = 0
        self.distance = 0
        self.parent = None

    def __setattr__(self, item, value):
        self.__dict__[item] = value
        return self

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return self.name

    def deg(self):
        return len(self.children)

class Graph():
    def __init__(self, vertices:list, edges:[tuple]):
        self.vertices = len(vertices)*[None]
        for i,v in enumerate(vertices):
            self.vertices[i] = Vertex(name=str(v))
        # edges are directed. undirected graphs will be represented by double edges
        self.edges = edges
        for e in self.edges:
            self.vertices[e[0]].children.append(self.vertices[e[1]])

    def bfs(self,root=None):
        if root is not None:
            ptr = root
        else:
            ptr = self.vertices[1]

        ptr.distance = 0
        q = deque([ptr])
        while len(q) > 0:
            ptr = q.popleft()
            print(ptr)

            q.extend(list(v.__setattr__('parent',ptr).__setattr__('distance',ptr.distance+1) for v in ptr.children if v.visited != 1))
            ptr.visited = 1

    def avg_degree(self):
        pass

if __name__ == '__main__':
    vertices = list(range(0,100))
    edges = random.sample(list(product(vertices,vertices)),500)
    g = Graph(vertices,edges)
    g.bfs()
