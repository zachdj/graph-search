# The Path class represents paths on a graph and records the total path cost


class Path:
    def __init__(self):
        self.length = 0
        self.cost = 0
        self.nodes = []

    def add_node(self, node_label, cost):
        self.length += 1
        self.cost += cost
        self.nodes.append(node_label)

    def __str__(self):
        return " -> ".join(self.nodes) + "\n Cost: %s" % self.cost
