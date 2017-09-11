# The Path class represents paths on a graph and records the total path cost


class Path:
    def __init__(self):
        self.length = 0
        self.cost = 0
        self.nodes = []

    # adds a node to the end of the path
    def add_node(self, node_label, cost):
        self.length += 1
        self.cost += cost
        self.nodes.append(node_label)

    # reverses the path (this is useful when building Paths from child to parent)
    def reverse(self):
        self.nodes.reverse()

    def __str__(self):
        return " -> ".join(self.nodes) + "\t (Cost: %s)" % self.cost
