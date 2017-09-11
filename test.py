from pygraphml import GraphMLParser
from Problem import Problem
from searchers.Uninformed import bfs, dfs, iterative_deepening, ucs


parser = GraphMLParser()
graph = parser.parse("test-graphs/test2.graphml")
# for edge in graph.edges():
#     edge.set_directed(True)

start_node_label = "A"

def goal_test(node):
    # print("testing node " + node['label'])
    acceptable = set(['I', 'O', 'Q'])
    return node['label'] in acceptable

problem = Problem(graph, start_node_label, goal_test)

# solution = dfs(problem, 4)
# solution = bfs(problem)
solution = ucs(problem)
# solution = iterative_deepening(problem)
print("Solution: " + solution.__str__())