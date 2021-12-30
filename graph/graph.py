# An efficient graph implementation that uses an adjacency list to represent vertices and edges.
# Implementation passes all tests in test_graph.py
# @author jcanepa


class Graph:
    def __init__(self):
        self.data = {}

    def adjacent(self, a, b):
        if not (self.vertex_exists(a) and self.vertex_exists(b)):
            return False
        return b in self.neighbors(a)

    def neighbors(self, vertex):
        return self.data[vertex] if self.vertex_exists(vertex) \
            else []

    def add_vertex(self, vertex):
        if not self.vertex_exists(vertex):
            self.data[vertex] = []

    def remove_vertex(self, vertex):
        if self.vertex_exists(vertex):

            for neighbor in self.data[vertex]:
                self.data[neighbor].remove(vertex)

            del self.data[vertex]

    def add_edge(self, a, b):
        if (self.vertex_exists(a) and self.vertex_exists(b)) \
            and not self.adjacent(a, b):
            self.data[a].append(b)
            self.data[b].append(a)

    def remove_edge(self, a, b):
        if (self.vertex_exists(a) and self.vertex_exists(b)) \
            and self.adjacent(a, b):
            self.data[a].remove(b)
            self.data[b].remove(a)

    def v(self):
        return len(self.data.items())

    def e(self):
        edges = 0
        for key, neighbors in self.data.items():
            edges += len(neighbors)
        return edges / 2

    def vertex_exists(self, vertex):
        return vertex in self.data.keys()