#!/usr/bin/python
'''
  week1.successor.py
  @author: recardona
'''

class SuccessorFunction(object):
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
        
        However, states may not be mapped to the same action with different
        resulting states; the Successor Function will replace the mapping if
        such a mapping attempt is made.
        
        Returns self for method chaining.
        """
        if not self.mapping.has_key(state):
            self.mapping[state] = {(action, resulting_state)}
            
        else:
            existing_mappings = self.mapping[state]
            new_mapping = {(action, resulting_state)}
            resulting_state_to_delete = None
            
            for mapped_action, resulting_state in existing_mappings:
                if mapped_action == action:  #you're trying to add an action with a different resulting_state
                    resulting_state_to_delete = resulting_state  #note the old resulting_state for deletion
            
            if resulting_state_to_delete is not None:
                existing_mappings.remove((action, resulting_state_to_delete)) #delete old resulting_state
            
            existing_mappings.update(new_mapping)
            self.mapping[state] = existing_mappings
        
        return self
    
    def getApplicableActionsInState(self, state):
        """
        Returns the Set of Actions (only) that are applicable in the parameter
        State. If none are applicable as defined by the function, returns None.
        """
        if not self.mapping.has_key(state):
            return None
        
        else:
            applicable_actions = set()
            existing_mappings  = self.mapping[state] #set of (action, resulting_state) pairs
            for action_state_pair in existing_mappings:
                applicable_actions.update({action_state_pair[0]}) #extract the action
            
            return applicable_actions
            
        pass
            
    def resolveActionInState(self, state, action):
        """
        Returns the State that results from applying the given Action in the
        given State.  If no such given State is mapped, or the given Action
        cannot be applied in the given State, this method returns None. 
        """
        if not self.mapping.has_key(state):
            return None
        
        resulting_state = None
        existing_mappings = self.mapping[state]
        
        for mapping in existing_mappings:
            if mapping[0] == action:
                resulting_state = mapping[1]
                
                
        return resulting_state
    
    
    
