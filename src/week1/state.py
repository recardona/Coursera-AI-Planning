'''
Created on Feb 16, 2013

@author: recardon
'''

class State():
    """
    Represents a set of conditions that hold in the world.  In this
    representation, a name is sufficient to define a state, however, you may
    define an optional set of parameters that hold true at that world state.  
    
    States are defined with the Closed World Assumption in mind.  That is, when
    using States that carry with them conditions, any conditions that are not
    included are assumed to be false (that is, these conditions do not hold in
    the world).
    """
    
    def __init__(self, name = "Dummy", conditions = {}):
        self.name = name
        self.conditions = conditions
        
    def __str__(self):
        conditions_string = "(None)"
        
        if(len(self.conditions) > 0):
            conditions_string = self.conditions
        
        return "State {0} with conditions: {1}".format(self.name, conditions_string)
        
    def __hash__(self):
        """
        Defined for use in the Successor Function (@see: successor.py)
        """
        hash_value = hash(self.name)
        
        for condition_key in self.conditions.keys():
            hash_value += hash(condition_key)
            condition_values = self.conditions[condition_key]
            
            for value in condition_values:
                hash_value += hash(value)
        
        return hash_value
    
    def __eq__(self, other):
        """
        State equality must have equality in the names and the conditions (if any)
        """
        if(not isinstance(other, State)):
            return False
        
        if(self.name != other.name):
            return False
        
        if(self.conditions != other.conditions):
            return False
        
        return True
        
    def __ne__(self, other):
        """
        State inequality must have inequality in the names and the conditions (if any)
        """
        return not self.__eq__(other)
        
            
    
    