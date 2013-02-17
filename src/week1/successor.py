'''
Created on Feb 17, 2013

@author: recardona
'''

class SuccessorFunction():
    '''
    A Successor Function is a function that returns all Actions that are
    applicable in a given State.  Each Action is tied to a State that results
    from having applied the corresponding Action.
    
    In other words, it is a mapping between:
        State -> (Action, State)
    '''


    def __init__(self, mapping = {}):
        '''
        Initializes a Successor Function, implemented as a map internally.  
        '''
        self.mapping = mapping
        
    def __str__(self):
        successor_function_string = "Successor Function: \n"
        
        for key in self.mapping.keys():
            successor_function_string += "({0}) -> \n".format(key)
            
            for value in self.mapping[key]:
                successor_function_string += "\t ({0}, {1})\n".format(value[0],value[1])
                
        return successor_function_string
    
    def __len__(self):
        return len(self.mapping)
    
    def addMapping(self, state, action, resulting_state):
        """
        Adds the mapping state -> (action, resulting_state) to this function.
        
        A Successor Function is a multivalued function; states can be mapped to
        multiple (action, resulting_state) pairs.
        
        Returns self for method chaining.
        """
        if not self.mapping.has_key(state):
            self.mapping[state] = {(action, resulting_state)}
            
        else:
            existing_mappings = self.mapping[state]
            new_mapping = {(action, resulting_state)}
            existing_mappings.update(new_mapping)
            self.mapping[state] = existing_mappings
        
        return self
    
