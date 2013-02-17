'''
Created on Feb 16, 2013

@author: recardon
'''

class Action():
    """
    Represents things an agent can do to change the state of the world.  In
    this representation, a name is the only thing that defines an action.
    """
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "Action {0}".format(self.name);
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        """
        Action equality relies on type and name equality.
        """
        if(not isinstance(other, Action)):
            return False
        
        if(self.name != other.name):
            return False
        
        return True
        
    def __ne__(self, other):
        """
        Action inequality must have inequality in the type or name
        """
        return not self.__eq__(other)
        
        