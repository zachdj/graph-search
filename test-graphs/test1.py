# basic binary tree with all edge weights = 1

from pygraphml import Graph, GraphMLParser

test1 = Graph()

a = test1.add_node("A")
b = test1.add_node("B")
c = test1.add_node("C")
d = test1.add_node("D")
e = test1.add_node("E")
f = test1.add_node("F")
g = test1.add_node("G")
h = test1.add_node("H")
i = test1.add_node("I")
j = test1.add_node("J")
k = test1.add_node("K")
l = test1.add_node("L")
m = test1.add_node("M")
n = test1.add_node("N")
o = test1.add_node("O")

test1.add_edge(a, b, directed=True)
test1.add_edge(a, c, directed=True)
test1.add_edge(b, d, directed=True)
test1.add_edge(b, e, directed=True)
test1.add_edge(c, f, directed=True)
test1.add_edge(c, g, directed=True)
test1.add_edge(d, h, directed=True)
test1.add_edge(d, i, directed=True)
test1.add_edge(e, j, directed=True)
test1.add_edge(e, k, directed=True)
test1.add_edge(f, l, directed=True)
test1.add_edge(f, m, directed=True)
test1.add_edge(g, n, directed=True)
test1.add_edge(g, o, directed=True)

for edge in test1.edges():
    edge['weight'] = 1

parser = GraphMLParser()
parser.write(test1, "test1.graphml")
