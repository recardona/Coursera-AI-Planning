'''
Created on Feb 16, 2013

@author: recardon
'''

class SearchNode(object):
    """
    A Search Node is a data structure that we manipulate during the search
    process.  Search nodes are nodes in the search tree.  It is characterized
    by the state it represents, a parent node, the action that gets us from
    the parent node's state to this state, the path cost of reaching this node
    and the depth of this node in the search tree.
    """
    
    def __init__(self, state, parent_node=None, action=None, path_cost=0, depth=0):
        """
        Initializes a SearchNode with the given parameters.  Default parameters
        are for when the node is the root node of the search tree.
        """
        self.state = state
        self.parent_node = parent_node 
        self.action = action
        self.path_cost = path_cost
        self.depth = depth 

    def __str__(self):
        if self.isRoot():
            return "Root SearchNode for State: {0}".format(self.state)
        
        else:
            return "SearchNode for State: {0}, with parent {1} through Action \
            {2}\n\tPath Cost: {3}\t\tDepth:{4}".format(self.state, \
                                                       self.parent_node.state, \
                                                       self.path_cost, self.depth)
    
    def isRoot(self):
        return (self.parent_node == None and self.action == None and \
                self.path_cost == 0 and self.depth == 0)


class SearchProblem(object):
    """
    A Search Problem is characterized by an initial state, a set of possible
    actions and applicability conditions, a goal state, and a path cost
    function.
    """
    
    def __init__(self, init_state, successor_function, goal_state, \
                 path_cost_function=lambda state: state.depth*1):
        """
        The Search Problem is defined by an initial state, a successor function,
        and a goal state.  In lieu of a path cost function, a default one is
        provided that depends on the depth of the node in the tree.
        """
        self.initState = init_state
        self.successorFunction = successor_function
        self.goalState = goal_state
        self.pathCostFunction  = path_cost_function
        pass
    
    def __str__(self):
        return "Problem: Get from State {} to State {}".format(self.initState, self.goalState)
        
    def goalTest(self, search_node):
        """
        Checks whether or not the given SearchNode is the goal.
        returns True iff it is of type SearchNode and its State is the goal.
        """
        if type(search_node) is not SearchNode:
            return False
        
        else:
            if search_node.state == self.goalState:
                return True
            
            else:
                return False
            
            
        
    
    
