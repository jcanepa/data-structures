# Scratchpad for tinkering with the graph class.
# @author jcanepa

from graph import Graph


# Example
g = Graph()
g.data['A'] = ['B']
g.data['B'] = ['A']
print(g)

print(g.adjacent('A', 'B')) # should be true
print(g.adjacent('A', 'FAKE')) # f
print(g.adjacent('B', 'A')) # f

g.remove_vertex('A')
