from pygraphml import GraphMLParser
from Problem import Problem
import searchers.Uninformed as Uninformed, searchers.Informed as Informed

parser = GraphMLParser()


# Romania problem from the textbook:
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

print("A* solution for the Romania problem:")
print(romania_sln)