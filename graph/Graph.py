from pygraphml import Graph as MLGraph

"""
    The Graph class serves as a wrapper around pygraphml graphs.
    It contains high-level methods to add nodes, add edges, and read/write graphs from a file using GraphML format.
    By default, all graphs are weighted.  Edge weights will default to 1 if a weight is not specified.
    
    Graphs are undirected by default, but can be changed to directed-only using the 'is_directed' constructor argument
"""


class Graph(object):
    default_edge_weight = 1

    def __init__(self, is_directed=False):
        self.is_directed = is_directed
        self.loaded_from_file = False
        self.filename = None

        self.graph = MLGraph()
        self.nodes = dict()
        self.edges = dict()

    # adds a node to the graph with the label specified by 'id'.  Each node must have a unique label
    # returns the node object created by pygraphml
    def add_node(self, id):
        stringified_id = str(id)
        if id not in self.nodes:
            node_object = self.graph.add_node(stringified_id)
            self.nodes[stringified_id] = node_object
            return node_object
        else:
            raise Exception("Duplicate node insertion attempted.  Node id '%s'" % stringified_id)

    # adds an edge to the graph with the specified weight
    # if the graph is directed, the edge will be an arc from node1 to node2
    def add_edge(self, node1, node2, weight=default_edge_weight):
        a, b = node1, node2

        # TODO: need to check if edge already exists

        # TODO: need better type-checking for node1 and node2

        if type(node1) is str and node1 in self.nodes:
            a = self.nodes[node1]

        if type(node2) is str and node2 in self.nodes:
            b = self.nodes[node2]

        edge_object = self.graph.add_edge(a, b, directed=self.is_directed)
        edge_object['weight'] = weight

        edge_key = a['label'] + b['label']
        self.edges[edge_key] = edge_object

        return edge_object
