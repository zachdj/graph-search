from SearchNode import SearchNode
from Queue import PriorityQueue

"""
    Performs a greedy search on the given problem using the provided heuristic function
    
    heuristic should be a function h(p, n) that returns an estimate for the distance from node n to the 
    solution of problem p. It will be passed the problem and the current node.
"""
def greedy(problem, heuristic):
    current_node = SearchNode(problem.start_node, None, 0)
    frontier = PriorityQueue()
    # elements of the priority queue are 2-element lists of the form (priority, data)
    frontier.put([0, current_node])
    explored = set()

    while True:
        if frontier.empty():
            return None
        queue_element = frontier.get()
        current_node = queue_element[1]
        # goal test
        if problem.goal_test(current_node.node):
            return current_node.to_path()  # return solution as path

        # add node ID to explored set
        explored.add(current_node.node.id)

        for edge in current_node.node.edges():
            child = None
            if edge.child().id != current_node.node.id:
                child = edge.child()
            elif not edge.directed() and edge.parent().id != current_node.node.id:
                child = edge.parent()

            if child is not None:
                weight = float(edge['weight'])
                child_node = SearchNode(child, current_node, weight)
                fn = heuristic(problem, child)  # value given by the evaluation function for this node

                # check that child is not in explored or frontier
                child_in_explored = child.id in explored
                child_in_frontier = False
                for item in frontier.queue:
                    if item[1].node.id == child.id:
                        child_in_frontier = True
                        # if the child has a lower heuristic score, replace the frontier node with child
                        if fn < item[0]:
                            item[0] = fn
                            item[1] = child_node

                if not child_in_explored and not child_in_frontier:
                    frontier.put([fn, child_node])


"""
    Performs A* search on the given problem using the given heuristic function
    
    heuristic should be a function h(p, n) that returns an estimate for the distance from node n to the 
    solution of problem p. It will be passed the problem and the current node.
"""
def a_star(problem, heuristic):
    current_node = SearchNode(problem.start_node, None, 0)
    frontier = PriorityQueue()
    # elements of the priority queue are 2-element lists of the form (priority, data)
    frontier.put([0, current_node])
    explored = set()

    while True:
        if frontier.empty():
            return None
        queue_element = frontier.get()
        current_node = queue_element[1]
        current_node_path_cost = current_node.get_path_cost()
        # goal test
        if problem.goal_test(current_node.node):
            return current_node.to_path()  # return solution as path

        # add node ID to explored set
        explored.add(current_node.node.id)

        for edge in current_node.node.edges():
            child = None
            if edge.child().id != current_node.node.id:
                child = edge.child()
            elif not edge.directed() and edge.parent().id != current_node.node.id:
                child = edge.parent()

            if child is not None:
                weight = float(edge['weight'])
                child_node = SearchNode(child, current_node, weight)
                child_path_cost = current_node_path_cost + weight
                fn = child_path_cost + heuristic(problem, child)

                # check that child is not in explored or frontier
                child_in_explored = child.id in explored
                child_in_frontier = False
                for item in frontier.queue:
                    if item[1].node.id == child.id:
                        child_in_frontier = True
                        # if the child has a lower evaluation, replace the frontier node with child
                        if fn < item[0]:
                            item[0] = fn
                            item[1] = child_node

                if not child_in_explored and not child_in_frontier:
                    frontier.put([fn, child_node])
