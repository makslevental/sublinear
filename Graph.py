import numpy as np
from collections import deque
from functools import partial

def universal_sink(mat):

    shp = np.shape(mat)
    i = 0
    j = 1
    while i < shp[0] and j < shp[1]:
        if mat[i,j] == 0:
            j += 1
        elif mat[i,j] == 1:
            i += 1

    if i == 0:
        check = True
        for k in range(0,shp[0]):
            if mat[k,0] == 0:
                check = False
    elif i == shp[0]:
        check = True
        for k in range(0,i):
            if mat[k,j] == 0:
                check = False
    else:
        check = False

    return check


class Vertex():
    def __init__(self,name:str=None,value=None,children:dict=None):
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if children is not None:
            self.children = children
        else:
            self.children = set()

        self.visited = 0
        self.distance = 0
        self.parent = None

    def __setattr__(self, item, value):
        setattr(self,item,value)
        return self

    def deg(self):
        return len(self.children)

class Graph():
    def __init__(self, vertices, edges):
        self.vertices = {}
        for v in vertices:
            self.vertices[v] = Vertex(name=str(v))
        # edges are directed. undirected graphs will be represented by double edges
        self.edges = edges
        for e in self.edges:
            self.vertices[e[1]].children.add(self.vertices[e[2]])

    def bfs(self,root=None):
        if root is not None:
            ptr = root
        else:
            ptr = self.vertices[1]

        ptr.distance = 0
        ptr.parent = None
        q = deque([ptr])
        while len(q) > 0:
            ptr = q.popleft()
            q.append(setattr(setattr(v,'parent',ptr),'distance',ptr.distance+1) for v in ptr.children if v.visited != 1)
            ptr.visited = 1

    def avg_degree(self):
        pass

