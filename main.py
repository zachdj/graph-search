from pygraphml import Graph
# main file - runs experiments/tests
g = Graph()
test_node1 = g.add_node("test1")
test_node2 = g.add_node("test2")
test_edge = g.add_edge(test_node1, test_node2)
test_edge['weight'] = 5

print(test_edge)