from Path import Path


"""
    A SearchNode object represents a node in the graph but keeps track of the parent node and the cost to jump from parent to child
    node should be a pygraphml Node object
    parent should be another search node
    cost should be the weight of the (parent, child) edge
"""
class SearchNode:
    def __init__(self, node, parent, cost):
        self.node = node
        self.parent = parent
        self.cost = cost

    # converts this SearchNode to a Path object representing the path leading to the current node
    def to_path(self):
        path = Path()
        child = self.node
        parent = self.parent
        cost = self.cost

        path.add_node(child['label'], cost)
        while parent is not None:
            child = parent.node
            cost = parent.cost
            parent = parent.parent

            path.add_node(child['label'], cost)

        path.reverse()
        return path

    def get_path_cost(self):
        parent = self.parent
        cost = self.cost

        while parent is not None:
            cost += parent.cost
            parent = parent.parent

        return cost
