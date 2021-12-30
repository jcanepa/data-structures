# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_graph

import unittest
import time
import random
import operator
from graph import Graph

class TestGraph(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A Graph exists.
        """
        try:
            Graph()
        except NameError:
            self.fail("Could not instantiate Graph.")

    def test_internal(self):
        """
        A graph uses an 'adjacency list' to represent vertices and edges.
        """
        g = Graph()
        self.assertEqual(dict, type(g.data))

    # """
    # Empty graphs.
    # """

    def test_adjacent_empty(self):
        """
        An empty graph has no vertices, so adjacent returns false.
        """
        g = Graph()
        self.assertFalse(g.adjacent('A', 'B'))

    def test_neighbors_empty(self):
        """
        Asking for the neighbors of any vertex in an empty graph returns an empty
        list.
        """
        g = Graph()
        self.assertEqual([], g.neighbors('A'))

    def test_add_vertex_empty(self):
        """
        When storing a new vertex, the graph associates an empty list of neighbors.
        """
        g = Graph()
        g.add_vertex('A')
        self.assertEqual([], g.data['A'])

    def test_remove_vertex_nonexistent(self):
        """
        When removing a vertex that does not exist, nothing happens.
        Hint: Just pass for now.
        """
        g = Graph()
        try:
            g.remove_vertex('A')
        except KeyError:
            self.fail('Removing a key raised an error.')
        self.assertEqual({}, g.data)

    def test_add_edge_nonexistent(self):
        """
        Adding an edge between two vertices that do not exist does nothing.
        Hint: Just pass for now.
        """
        g = Graph()
        try:
            g.add_edge('A', 'B')
        except KeyError:
            self.fail("Adding invalid edge raised a KeyError")

    def test_remove_edge_nonexistent(self):
        """
        Removing an edge that does not exist does nothing.
        Hint: Just pass for now.
        """
        g = Graph()
        try:
            g.remove_edge('A', 'B')
        except KeyError:
            self.fail("Removing nonexistent edge raised a KeyError")

    # """
    # Single-vertex graph.
    # """

    def test_adjacent_one(self):
        """
        A graph with one vertex has no neighbors, so adjacent returns false.
        """
        g = Graph()
        g.data['A'] = []
        self.assertFalse(g.adjacent('A', 'B'))
        self.assertFalse(g.adjacent('A', 'FAKE'))

    def test_neighbors_one(self):
        """
        Asking for the neighbors of a vertex in an graph with just one vertex
        returns an empty list.
        """
        g = Graph()
        g.data['A'] = []
        self.assertEqual([], g.neighbors('A'))

    def test_add_vertex_one(self):
        """
        When storing a new vertex in a graph with a single vertex, the graph
        adds the new vertex and associates an empty list of neighbors.
        """
        g = Graph()
        g.data['A'] = []
        g.add_vertex('B')
        self.assertEqual([], g.data['B'])
        self.assertEqual([], g.data['A'])

    def test_add_vertex_existing(self):
        """
        When adding a vertex that already exists, the graph does not modify the
        existing vertex.
        """
        g = Graph()
        g.data['A'] = ['FAKE']
        g.add_vertex('A')
        self.assertEqual(['FAKE'], g.data['A'])

    def test_remove_vertex_one(self):
        """
        Removing a vertex from a graph removes its entry from the graph's
        adjacency list.
        """
        g = Graph()
        g.data['A'] = []
        g.remove_vertex('A')
        self.assertRaises(KeyError, operator.itemgetter('A'), g.data)

    def test_add_edge_one(self):
        """
        Adding an edge between an existing vertex and one that does not exist
        does nothing.
        """
        g = Graph()
        g.data['A'] = []
        try:
            g.add_edge('A', 'B')
        except KeyError:
            self.fail("Adding invalid edge raised a KeyError")

    def test_remove_edge_one(self):
        """
        Removing an edge that does not exist does nothing.
        """
        g = Graph()
        g.data['A'] = []
        try:
            g.remove_edge('A', 'B')
        except KeyError:
            self.fail("Removing nonexistent edge raised a KeyError")

    # """
    # Graphs with two vertices.
    # """

    def test_adjacent_two(self):
        """
        A vertex, v2, is a neighbor of v1 when v2 is present in v1's list of neighbors.
        Note: Neighbors should indeed be present in each others' list of neighbors,
        but this isn't the job of the `adjacent` method.
        """
        g = Graph()
        g.data['A'] = ['B']
        g.data['B'] = []  # Intentionally minimal. See the Note above.
        self.assertTrue(g.adjacent('A', 'B'))
        self.assertFalse(g.adjacent('A', 'FAKE'))
        self.assertFalse(g.adjacent('B', 'A'))

    def test_neighbors_two(self):
        """
        Asking for the neighbors of any vertex returns a list of its neighbors.
        """
        g = Graph()
        g.data['A'] = ['B', 'FAKE']
        g.data['B'] = ['A']
        self.assertEqual(['B', 'FAKE'], g.neighbors('A'))
        self.assertEqual(['A'], g.neighbors('B'))
        self.assertEqual([], g.neighbors('FAKE'))

    def test_remove_vertex_two(self):
        """
        Removing a vertex also removes it from all vertex neighbors lists.
        """
        g = Graph()
        g.data['A'] = ['B']
        g.data['B'] = ['A']
        g.remove_vertex('A')
        self.assertRaises(KeyError, operator.itemgetter('A'), g.data)
        self.assertEqual([], g.data['B'])

    def test_add_edge_two(self):
        """
        Adding an edge between two vertices adds each vertex to both of their
        neighbor lists.
        """
        g = Graph()
        g.data['A'] = []
        g.data['B'] = []
        g.add_edge('A', 'B')
        self.assertEqual(['B'], g.data['A'])
        self.assertEqual(['A'], g.data['B'])
        g.data['A'] = []
        g.data['B'] = []
        g.add_edge('B', 'A')
        self.assertEqual(['B'], g.data['A'])
        self.assertEqual(['A'], g.data['B'])

    def test_add_edge_existing_two(self):
        """
        Adding an edge to vertices that already share and edge does not create a
        second edge.
        """
        g = Graph()
        g.data['A'] = ['B']
        g.data['B'] = ['A']
        g.add_edge('A', 'B')
        self.assertEqual(['B'], g.data['A'])
        self.assertEqual(['A'], g.data['B'])

    def test_remove_edge_two(self):
        """
        Removing an edge between two vertices removes each vertex from both
        neighbors lists.
        """
        g = Graph()
        g.data['A'] = ['B']
        g.data['B'] = ['A']
        g.remove_edge('A', 'B')
        self.assertEqual([], g.data['A'])
        self.assertEqual([], g.data['B'])
        g.data['A'] = ['B']
        g.data['B'] = ['A']
        g.remove_edge('B', 'A')
        self.assertEqual([], g.data['A'])
        self.assertEqual([], g.data['B'])

    def test_remove_edge_nonexisting_two(self):
        """
        Removing an edge that does not exist does nothing.
        """
        g = Graph()
        g.data['A'] = ['FAKE']
        g.data['B'] = ['FAKE 2']
        g.remove_edge('A', 'B')
        g.remove_edge('B', 'A')
        self.assertEqual(['FAKE'], g.data['A'])
        self.assertEqual(['FAKE 2'], g.data['B'])

    # """
    # Larger graphs
    # """

    def test_adjacent(self):
        """
        Two vertices are adjacent if they share an edge.
        """
        g = larger_graph()
        self.assertTrue(g.adjacent('A', 'B'))
        self.assertTrue(g.adjacent('B', 'A'))
        self.assertTrue(g.adjacent('A', 'C'))
        self.assertTrue(g.adjacent('C', 'A'))
        self.assertTrue(g.adjacent('A', 'D'))
        self.assertTrue(g.adjacent('D', 'A'))
        self.assertTrue(g.adjacent('B', 'C'))
        self.assertTrue(g.adjacent('C', 'B'))
        self.assertFalse(g.adjacent('B', 'D'))
        self.assertFalse(g.adjacent('D', 'B'))
        self.assertFalse(g.adjacent('C', 'D'))
        self.assertFalse(g.adjacent('D', 'C'))

    def test_neighbors(self):
        """
        Vertices that share an edge are neighbors.
        """
        g = larger_graph()
        self.assertEqual(['B', 'C', 'D'], g.neighbors('A'))
        self.assertEqual(['A', 'C'], g.neighbors('B'))
        self.assertEqual(['A', 'B'], g.neighbors('C'))
        self.assertEqual(['A'], g.neighbors('D'))

    def test_add_vertex(self):
        """
        Adding a vertex to a graph only creates a new entry in the adjacency list.
        """
        g = larger_graph()
        g.add_vertex('E')
        self.assertEqual([], g.data['E'])
        self.assertEqual(['B', 'C', 'D'], g.data['A'])
        self.assertEqual(['A', 'C'], g.data['B'])
        self.assertEqual(['A', 'B'], g.data['C'])
        self.assertEqual(['A'], g.data['D'])

    def test_remove_vertex(self):
        """
        Removing a vertex also removes its edges.
        Hint: Be efficient. Traversing all the vertices (keys) is inefficient.
        """
        g = larger_graph()
        g.remove_vertex('A')
        self.assertEqual(['C'], g.data['B'])
        self.assertEqual(['B'], g.data['C'])
        self.assertEqual([], g.data['D'])

    def test_add_edge(self):
        """
        Adding an edge between two vertices connects them as adjacent neighbors.
        """
        g = larger_graph()
        g.add_edge('D', 'B')
        self.assertEqual(['A', 'C', 'D'], g.data['B'])
        self.assertEqual(['A', 'B'], g.data['D'])
        self.assertTrue(g.adjacent('B', 'D'))
        self.assertTrue(g.adjacent('D', 'B'))
        self.assertEqual(['B', 'C', 'D'], g.data['A'])
        self.assertEqual(['A', 'B'], g.data['C'])

    def test_remove_edge(self):
        """
        Removing an edge disconnects two vertices.
        """
        g = larger_graph()
        g.remove_edge('A', 'B')
        self.assertEqual(['C', 'D'], g.data['A'])
        self.assertEqual(['C'], g.data['B'])
        self.assertFalse(g.adjacent('A', 'B'))
        self.assertFalse(g.adjacent('B', 'A'))
        self.assertEqual(['A', 'B'], g.data['C'])
        self.assertEqual(['A'], g.data['D'])

    # """
    # Properties
    # """

    def test_v(self):
        """
        |V| is the number of vertices in a graph.
        """
        g = Graph()
        g.add_vertex('A')
        self.assertEqual(1, g.v())
        g.add_vertex('B')
        g.add_vertex('C')
        self.assertEqual(3, g.v())

    def test_e(self):
        """
        |E| is the number of edges in a graph.
        Hint: There's an easy way - read or look it up?
        Bonus: Try reduce.
        """
        g = larger_graph()
        self.assertEqual(4, g.e())
        g.add_edge('D', 'B')
        self.assertEqual(5, g.e())


def larger_graph():
    """
       B
       | \
    D--A--C
    """
    g = Graph()
    g.data['A'] = ['B', 'C', 'D']
    g.data['B'] = ['A', 'C']
    g.data['C'] = ['A', 'B']
    g.data['D'] = ['A']
    return g

def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
