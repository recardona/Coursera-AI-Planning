'''
Created on Feb 16, 2013

@author: recardon
'''

class SearchNode():
    """
    A Search Node is a data structure that we manipulate during the search
    process.  Search nodes are nodes in the search tree.  It is characterized
    by the state it represents, a parent node, the action that gets us from
    the parent node's state to this state, the path cost of reaching this node
    and the depth of this node in the search tree.
    """
    
    def __init__(self):
        pass

class SearchProblem():
    """
    A Search Problem is characterized by an initial state, a set of possible
    actions and applicability conditions, a goal state, and a path cost
    function.
    """
    
    def __init__(self, init_state, successor_function, goal_state, path_cost_function):
        self.initState = init_state
        self.successorFunction = successor_function
        self.goalState = goal_state
        self.pathCostFunction  = path_cost_function
        pass
    
    def __str__(self):
        "Problem: Get from State {} to State {}".format(self.initState, self.goalState)
    
    
