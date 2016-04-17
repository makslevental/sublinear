from collections import deque

class GraphError(Exception):
    def __init__(self, value):
        self.value = value

    def __str(self):
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
    def __init__(self, vertices:list, edges:[tuple]) -> None:
        self.vertices = len(vertices)*[None]
        for i,v in enumerate(vertices):
            self.vertices[i] = Vertex(name=str(v))
        # edges are directed. undirected graphs will be represented by double edges
        self.edges = edges
        for e in self.edges:
            self.vertices[e[0]].children.append(self.vertices[e[1]])

    def bfs(self, root:Vertex=None):
        ptr = root if root is not None else self.vertices[0]

        vert_order = []
        ptr.distance = 0
        q = deque([ptr])

        while len(q) > 0:
            ptr = q.popleft()
            if ptr.visited:
                continue
            else:
                vert_order.append(ptr)
                ptr.visited = True
                q.extend([v.set(parent=ptr, distance=ptr.distance+1)
                          for v in ptr.children if v.visited is not True])

        return vert_order

