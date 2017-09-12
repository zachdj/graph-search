from pygraphml import GraphMLParser
from Problem import Problem
import searchers.Uninformed as Uninformed, searchers.Informed as Informed

parser = GraphMLParser()


####### Romania problem from the textbook #######
def romania_goal_test(node):
    return node['label'] == 'Bucharest'

romania_sld_table = {
    'Arad':366,
    'Bucharest':0,
    'Craiova':160,
    'Drobeta':242,
    'Eforie':161,
    'Fagaras':176,
    'Giurgiu':77,
    'Hirsova':151,
    'Iasi':226,
    'Lugoj':244,

    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374

}
def romania_heuristic(problem, node):
    return romania_sld_table[ node['label'] ]

romania_graph = parser.parse("test-graphs/romania.graphml")

romania_start_node = "Arad"

romania_problem = Problem(romania_graph, romania_start_node, romania_goal_test)

romania_sln = Informed.a_star(romania_problem, romania_heuristic)
# romania_sln = Uninformed.ucs(romania_problem)

print("A* solution for the Romania problem: \n %s \n" % romania_sln)

####### Radiation problem from the HW1 #######
def radiation_goal_test(node):
    return node['label'] == '4'

# TODO: come up with a good heuristic for this problem
radiation_h_table = {
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': 0,
    '11': 0,
    '12': 0,
    '13': 0,
    '14': 0,
    '15': 0,

}
def radiation_heuristic(problem, node):
    return radiation_h_table[ node['label'] ]

radiation_graph = parser.parse("test-graphs/radiation.graphml")
# At the time of writing, the pygraphml parser is pretty bad and doesn't handle directed/undirected edges very well.
# so we have to manually make the edges directed here
for edge in radiation_graph.edges():
    edge.set_directed(True)

radiation_start_node = "13"

radiation_problem = Problem(radiation_graph, radiation_start_node, radiation_goal_test)

# radiation_sln = Informed.a_star(radiation_problem, radiation_heuristic)
radiation_sln = Uninformed.ucs(radiation_problem)

print("UCS solution for the Radiation problem: \n %s \n" % radiation_sln)