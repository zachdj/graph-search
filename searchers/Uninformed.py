from SearchNode import SearchNode
from Queue import Queue
from Queue import PriorityQueue

"""
    Performs a breadth-first search on the given problem
    Returns Path object representing the first solution found, or None if no solution could be found
"""
def bfs(problem):
    current_node = SearchNode(problem.start_node, None, 0)
    # check for solution
    if problem.goal_test(current_node.node):
        return current_node.to_path()

    # initialize frontier and explored set
    frontier = Queue()
    frontier.put(current_node)
    explored = set()

    while True:
        if frontier.empty():
            return None

        current_node = frontier.get()
        # add node ID to explored set
        explored.add(current_node.node.id)
        for edge in current_node.node.edges():
            child = None
            """
                Some explanation is warranted here.  Consider an edge (a, b).  When iterating over the edges of node b,
                (a, b) will show up as an edge.  If the edge is directed, then node a should not be considered a "child" of b
                However, if the edge is undirected, then node a IS a child of b
            """
            if edge.child().id != current_node.node.id:
                child = edge.child()
            elif not edge.directed() and edge.parent().id != current_node.node.id:
                child = edge.parent()

            if child is not None:
                weight = float(edge['weight'])
                child_node = SearchNode(child, current_node, weight)
                # check that child is not in explored or frontier
                child_found = False
                for item in frontier.queue:
                    if item.node.id == child.id:
                        child_found = True

                if child.id in explored:
                    child_found = True

                if not child_found:
                    # goal test
                    if problem.goal_test(child):
                        return child_node.to_path()
                    # insert child into the frontier
                    frontier.put(child_node)


def ucs(problem):
    current_node = SearchNode(problem.start_node, None, 0)
    frontier = PriorityQueue()
    # elements of the priority queue are 2-element lists of the form (priority, data)
    frontier.put( [0, current_node] )
    explored = set()

    while True:
        if frontier.empty():
            return None
        queue_element = frontier.get()
        current_node = queue_element[1]
        current_node_path_cost = queue_element[0]
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
                child_path_cost = current_node_path_cost+weight

                # check that child is not in explored or frontier
                child_in_explored = child.id in explored
                child_in_frontier = False
                for item in frontier.queue:
                    if item[1].node.id == child.id:
                        child_in_frontier = True
                        # if the child has a lower path cost, replace the frontier node with child
                        if child_path_cost < item[0]:
                            item[0] = child_path_cost
                            item[1] = child_node

                if not child_in_explored and not child_in_frontier:
                    frontier.put( [child_path_cost, child_node] )



"""
    Performs a depth-first search on the given problen.  Supports optional depth limit.  
    A negative depth limit (default) will allow the search to continue indefinitely
    
    Returns Path object representing the first solution found, or the DFS_CUTOFF_VALUE if the depth limit was 
    encountered without finding a solution, or None if no solution could be found
"""
DFS_CUTOFF_VALUE = "cutoff"  # special value returned if cutoff occurs


def dfs(problem, depth_limit = -1):
    start_node = SearchNode(problem.start_node, None, 0)
    return dfs_recursive(start_node, problem, depth_limit)


def dfs_recursive(node, problem, limit):
    if problem.goal_test(node.node):
        return node.to_path()
    elif limit == 0:  # depth limit has been reached without finding a solution
        return DFS_CUTOFF_VALUE
    else:
        cutoff_occurred = False
        for edge in node.node.edges():
            child = None
            # see comment in the definition of BFS for explanation of child definition logic
            if edge.child().id != node.node.id:
                child = edge.child()
            elif not edge.directed() and edge.parent().id != node.node.id:
                child = edge.parent()

            if child is not None:
                weight = float(edge['weight'])
                child_node = SearchNode(child, node, weight)
                result = dfs_recursive(child_node, problem, limit-1)

                if result == DFS_CUTOFF_VALUE:
                    cutoff_occurred = True
                elif result is not None:
                    return result
        if cutoff_occurred:
            return DFS_CUTOFF_VALUE  # no solution in the depth limit
        else:
            return None  # no solution in the graph


"""
    Performs an iterative deepening search on the given problem
    
    Returns Path object representing the first solution found, or None if no solution could be found
"""
def iterative_deepening(problem):
    depth = 0
    while True:
        result = dfs(problem, depth_limit=depth)
        if result != DFS_CUTOFF_VALUE:
            return result

        depth += 1
