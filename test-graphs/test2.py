# binary tree with a "deep and cheap" left half and an expensive but shallow right half

# TODO: make this graph directed
from pygraphml import Graph, GraphMLParser

test2 = Graph()

a = test2.add_node("A")
b = test2.add_node("B")
c = test2.add_node("C")
d = test2.add_node("D")
e = test2.add_node("E")
f = test2.add_node("F")
g = test2.add_node("G")
h = test2.add_node("H")
i = test2.add_node("I")
j = test2.add_node("J")
k = test2.add_node("K")
l = test2.add_node("L")
m = test2.add_node("M")
n = test2.add_node("N")
o = test2.add_node("O")
p = test2.add_node("P")
q = test2.add_node("Q")
r = test2.add_node("R")
s = test2.add_node("S")

test2.add_edge(a, b, directed=False)
test2.add_edge(b, c, directed=False)
test2.add_edge(b, d, directed=False)
test2.add_edge(c, e, directed=False)
test2.add_edge(c, f, directed=False)
test2.add_edge(d, g, directed=False)
test2.add_edge(d, h, directed=False)
test2.add_edge(f, i, directed=False)
test2.add_edge(f, j, directed=False)
test2.add_edge(g, k, directed=False)
test2.add_edge(g, l, directed=False)

for edge in test2.edges():
    edge['weight'] = 1

test2.add_edge(a, m, directed=False)
test2.add_edge(m, n, directed=False)
test2.add_edge(m, o, directed=False)
test2.add_edge(n, p, directed=False)
test2.add_edge(n, q, directed=False)
test2.add_edge(o, r, directed=False)
test2.add_edge(o, s, directed=False)


for edge in test2.edges():
    if edge.child()['label'] in ['M', 'N', 'O', 'P', 'Q', 'R', 'S']:
        edge['weight'] = 3

parser = GraphMLParser()
parser.write(test2, "test2.graphml")
