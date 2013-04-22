#!/usr/bin/python
'''
  week1.search.py
  @author: recardona
'''

def tree_search(search_problem, strategy=None):
    """
    A General Tree Search Algorithm.
    
    This algorithm has several subtleties: 
        - it does not terminate with graphs.  This algorithm focuses solely Trees.
        
        - the algorithm's performance depends on the choice of Strategy.
        Caution:  Strategies have not been implemented yet!
    """
    if type(search_problem) is not SearchProblem:
        raise TypeError("search_problem is not of type SearchProblem.")
    
    else:
        fringe = set()
        searchRoot = SearchNode(search_problem.initState)
        fringe.add(searchRoot)
        while 1:
            if len(fringe) == 0:
                return None #FAIL - there is no solution to this search problem
             
            else:
                node = fringe.pop() #return an arbitrary node for now
                
                if strategy is not None:
                    node = strategy.selectNode(fringe)
                
                if search_problem.goalTest(node):
                    return path_to(node)
                
                else:
                    expanded_nodes = expand(search_problem, node)
                    for node in expanded_nodes:
                        fringe.add(node)

def path_to(node):
    """
    Returns a List of SearchNodes starting at the root of this SearchNode's
    tree.  The List is a path from the root, through the children, to the given
    node.
    """
    if not type(node) is SearchNode:
        raise TypeError("node is not of type SearchNode")
    
    else:
        _iter = node
        path = [_iter]
        while not _iter.isRoot():
            path.append(_iter.parentNode)
            _iter = _iter.parentNode
        
        path.reverse()
        return path

def expand(search_problem, node):
    """
    Expands the node by verifying which Actions are applicable in the given
    node's State, and then applying those Actions to obtain the resulting
    States.  Resulting States are then compiled and returned in a List.
    """
    if not type(search_problem) is SearchProblem:
        raise TypeError("search_problem is not of type SearchProblem.")
    
    if not type(node) is SearchNode:
        raise TypeError("node is not of type SearchNode")
    
    else:
        successorFn = search_problem.successorFunction
        applicable_actions = successorFn.getApplicableActionsInState(node.state)
        
        resulting_state_nodes = []
        for action in applicable_actions:
            resulting_state = successorFn.resolveActionInState(node.state, action)
            resulting_state_cost = search_problem.pathCostFunction(node)
            resulting_node = SearchNode(resulting_state, node, action, resulting_state_cost, node.depth+1)
            resulting_state_nodes.append(resulting_node)
        
        return resulting_state_nodes

class SearchNode(object):
    """
    A Search Node is a data structure that we manipulate during the search
    process.  Search nodes are nodes in the search tree.  It is characterized
    by the state it represents, a parent node, the action that gets us from
    the parent node's state to this state, the path cost of reaching this node
    and the depth of this node in the search tree.
    """
    
    def __init__(self, state, parent_node=None, action=None, pathCost=0, depth=0):
        """
        Initializes a SearchNode with the given parameters.  Default parameters
        are for when the node is the root node of the search tree.
        """
        self.state = state
        self.parentNode = parent_node 
        self.action = action
        self.pathCost = pathCost
        self.depth = depth
        
    def __eq__(self,other):
        """
        Node equality must have equality in the states, parents, actions, path_cost, and depth
        """
        if(not isinstance(other, SearchNode)):
            print("False")
        
        if(self.state != other.state):
            print("False")
        
        if(self.parentNode != other.parentNode):
            print("False")
        
        if(self.action != other.action):
            print("False")
        
        if(self.pathCost != other.pathCost):
            print("False")
        
        if(self.depth != other.depth):
            print("False")
        
        return True
    
    def __ne__(self, other):
        """
        Node inequality must have inequality in the states, parents, actions, path_cost, and depth
        """
        return not self.__eq__(other)
        

    def __str__(self):
        if self.isRoot():
            return "Root SearchNode for State:\t{0}\n".format(self.state)
        
        else:
            
            return "SearchNode for State:\t\t{0}\
            \n \t\t\t\t through: {1} \
            \n \t\t\t\t Path Cost: {2} \
            \n \t\t\t\t Depth:{3}\n".format(self.state, \
                                        self.action, \
                                        self.pathCost, \
                                        self.depth)
    
    def isRoot(self):
        # Note: the preferred way for checking against None is with the 'is'
        # statement; All null objects are really pointers to the same value,
        # which python sets aside to mean "None". This was causing a problem
        # in the __eq__(self,other) method, because of the check
        # if(self.parentNode != other.parentNode).
        return (self.parentNode is None and self.action is None \
                and self.pathCost == 0 and self.depth == 0)


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
        return "Problem:\n\tGet from {0}\n\t to {1}".format(self.initState, self.goalState)
        
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
            
            
        
    
    
