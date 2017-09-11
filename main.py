from pygraphml import Graph
from SearchNode import SearchNode
from Queue import Queue
# # main file - runs experiments/tests
g = Graph()
a = g.add_node("A")
b = g.add_node("B")
c = g.add_node("C")
edge = g.add_edge(a, b)

A = SearchNode(a, None, 0)
B = SearchNode(b, A, 2)
C = SearchNode(c, B, 3)

print(B.to_path())