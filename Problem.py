# problem objects are passed to searchers

class Problem:
    """
        graph is the pygraphml Graph object representing the problem
        start is the label of the node in the graph where the search will begin
        goal_test is a function that will be passed a pygraphml Node object and must return True if the node is a goal node
    """
    def __init__(self, graph, start, goal_test):

        self.graph = graph
        # find the node object with the given label
        self.start_node = None
        for node in graph.nodes():
            if node['label'] == start:
                self.start_node = node

        self.goal_test = goal_test
