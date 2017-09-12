# Radiation grid from CSCI 6550 HW 1

from pygraphml import Graph, GraphMLParser

radiation = Graph()

two = radiation.add_node("2")
three = radiation.add_node("3")
four = radiation.add_node("4")
six = radiation.add_node("6")
seven = radiation.add_node("7")
nine = radiation.add_node("9")
ten = radiation.add_node("10")
eleven = radiation.add_node("11")
twelve = radiation.add_node("12")
thirteen = radiation.add_node("13")
fourteen = radiation.add_node("14")
fifteen = radiation.add_node("15")

edge = radiation.add_edge(two, three, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(two, six, directed=True)
edge['weight'] = 11

edge = radiation.add_edge(three, two, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(three, four, directed=True)
edge['weight'] = 10
edge = radiation.add_edge(three, seven, directed=True)
edge['weight'] = 11

edge = radiation.add_edge(four, three, directed=True)
edge['weight'] = 9

edge = radiation.add_edge(six, two, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(six, seven, directed=True)
edge['weight'] = 11
edge = radiation.add_edge(six, ten, directed=True)
edge['weight'] = 9

edge = radiation.add_edge(seven, three, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(seven, six, directed=True)
edge['weight'] = 11
edge = radiation.add_edge(seven, eleven, directed=True)
edge['weight'] = 9

edge = radiation.add_edge(nine, ten, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(nine, thirteen, directed=True)
edge['weight'] = 7

edge = radiation.add_edge(ten, six, directed=True)
edge['weight'] = 11
edge = radiation.add_edge(ten, nine, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(ten, eleven, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(ten, fourteen, directed=True)
edge['weight'] = 7

edge = radiation.add_edge(eleven, seven, directed=True)
edge['weight'] = 11
edge = radiation.add_edge(eleven, ten, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(eleven, twelve, directed=True)
edge['weight'] = 10
edge = radiation.add_edge(eleven, fifteen, directed=True)
edge['weight'] = 8

edge = radiation.add_edge(twelve, eleven, directed=True)
edge['weight'] = 9

edge = radiation.add_edge(thirteen, nine, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(thirteen, fourteen, directed=True)
edge['weight'] = 7

edge = radiation.add_edge(fourteen, ten, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(fourteen, thirteen, directed=True)
edge['weight'] = 7
edge = radiation.add_edge(fourteen, fifteen, directed=True)
edge['weight'] = 8

edge = radiation.add_edge(fifteen, eleven, directed=True)
edge['weight'] = 9
edge = radiation.add_edge(fifteen, fourteen, directed=True)
edge['weight'] = 7

parser = GraphMLParser()
parser.write(radiation, "radiation.graphml")
