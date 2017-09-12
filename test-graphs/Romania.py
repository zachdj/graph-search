# Toy problem from the textbook: Romanian road map

from pygraphml import Graph, GraphMLParser

romania = Graph()

oradea = romania.add_node("Oradea")
zerind = romania.add_node("Zerind")
arad = romania.add_node("Arad")
sibiu = romania.add_node("Sibiu")
fagaras = romania.add_node("Fagaras")
timisoara = romania.add_node("Timisoara")
rv = romania.add_node("Rimnicu Vilcea")
lugoj = romania.add_node("Lugoj")
pitesti = romania.add_node("Pitesti")
mehadia = romania.add_node("Mehadia")
drobeta = romania.add_node("Drobeta")
craiova = romania.add_node("Craiova")
bucharest = romania.add_node("Bucharest")
giurgiu = romania.add_node("Giurgiu")
urziceni = romania.add_node("Urziceni")
neamt = romania.add_node("Neamt")
iasi = romania.add_node("Iasi")
vaslui = romania.add_node("Vaslui")
hirsova = romania.add_node("Hirsova")
eforie = romania.add_node("Eforie")

o2z = romania.add_edge(oradea, zerind, directed=False)
o2z['weight'] = 71

z2a = romania.add_edge(zerind, arad, directed=False)
z2a['weight'] = 75

o2s = romania.add_edge(oradea, sibiu, directed=False)
o2s['weight'] = 151

a2s = romania.add_edge(arad, sibiu, directed=False)
a2s['weight'] = 140

a2t = romania.add_edge(arad, timisoara, directed=False)
a2t['weight'] = 118

t2l = romania.add_edge(timisoara, lugoj, directed=False)
t2l['weight'] = 111

l2m = romania.add_edge(lugoj, mehadia, directed=False)
l2m['weight'] = 70

m2d = romania.add_edge(mehadia, drobeta, directed=False)
m2d['weight'] = 75

d2c = romania.add_edge(drobeta, craiova, directed=False)
d2c['weight'] = 120

s2r = romania.add_edge(sibiu, rv, directed=False)
s2r['weight'] = 80

r2c = romania.add_edge(rv, craiova, directed=False)
r2c['weight'] = 146

s2f = romania.add_edge(sibiu, fagaras, directed=False)
s2f['weight'] = 99

r2p = romania.add_edge(rv, pitesti, directed=False)
r2p['weight'] = 97

p2c = romania.add_edge(pitesti, craiova, directed=False)
p2c['weight'] = 138

f2b = romania.add_edge(fagaras, bucharest, directed=False)
f2b['weight'] = 211

p2b = romania.add_edge(pitesti, bucharest, directed=False)
p2b['weight'] = 101

b2g = romania.add_edge(bucharest, giurgiu, directed=False)
b2g['weight'] = 90

b2u = romania.add_edge(bucharest, urziceni, directed=False)
b2u['weight'] = 85

u2h = romania.add_edge(urziceni, hirsova, directed=False)
u2h['weight'] = 98

h2e = romania.add_edge(hirsova, eforie, directed=False)
h2e['weight'] = 86

u2v = romania.add_edge(urziceni, vaslui, directed=False)
u2v['weight'] = 142

v2i = romania.add_edge(vaslui, iasi, directed=False)
v2i['weight'] = 92

i2n = romania.add_edge(iasi, neamt, directed=False)
i2n['weight'] = 87


parser = GraphMLParser()
parser.write(romania, "romania.graphml")
