#!/usr/bin/python
'''
  week1.missionaries.py
  @author: recardona
'''

from search import tree_search
from search import SearchProblem
from action import Action
from state import State
from successor import SuccessorFunction


def main():
    
    move_one_missionary   = Action("1m")
    move_two_missionaries = Action("2m")
    move_one_cannibal     = Action("1c")
    move_two_cannibals    = Action("2c")
    move_one_and_one      = Action("1m1c") 
    
    initial_state = State("init", {'L':{'3m','3c','b'}, 'R':{'0m','0c'}})
    goal_state = State("goal", {'L':{'0m','0c'}, 'R':{'3m','3c','b'}})
    
    # Any state where cannibals outnumber missionaries is not a valid state
    one_and_one_over = State("1m1c Over", {'L':{'2m','2c'}, 'R':{'1m','1c','b'}})
    one_and_one_over_without_boat = State("1m1c Over w/o Boat", {'L':{'2m','2c','b'}, 'R':{'1m','1c'}})

    two_cannibals_over = State("2c Over", {'L':{'3m','1c'}, 'R':{'0m','2c','b'}})
    two_cannibals_over_without_boat = State("2c Over w/o Boat", {'L':{'3m','1c', 'b'}, 'R':{'0m','2c'}})

    one_cannibal_over = State("1c Over", {'L':{'3m','2c'}, 'R':{'0m','1c','b'}})
    one_cannibal_over_without_boat = State("1c Over w/o Boat", {'L':{'3m','2c','b'}, 'R':{'0m','1c'}})
    
    two_and_two_over = State("2m2c Over", {'L':{'1m','1c'}, 'R':{'2m','2c','b'}})
    two_and_two_over_without_boat = State("2m2c Over", {'L':{'1m','1c','b'}, 'R':{'2m','2c'}})
    
    three_cannibals_over = State("3c Over", {'L':{'3m','0c'}, 'R':{'0m','3c','b'}})
    three_missionaries_over_without_boat = State("3m Over w/o Boat", {'L':{'0m','3c', 'b'}, 'R':{'3m','0c'}})
    
    three_missionaries_one_cannibal_over = State("3m3c Over", {'L':{'0m','1c'}, 'R':{'3m','1c','b'}})
    three_missionaries_one_cannibal_over_without_boat = State("3m1c Over w/o Boat", {'L':{'0m','2c', 'b'}, 'R':{'3m','1c'}})
    
    three_missionaries_two_cannibals_over = State("3m2c Over", {'L':{'0m','1c'}, 'R':{'3m','2c','b'}})
    
    
    #Example invalid states:
    #two_cannibals_over_without_boat = State("2c Over w/o Boat", {'L':{'3m','1c', 'b'}, 'R':{'0m','2c'}})
    #one_missionary_two_cannibals_over = State("1m2c Over", {'L':{'2m','1c'}, 'R':{'1m','2c','b'}})
    
    #Successor Function
    successor_fn = SuccessorFunction()
    successor_fn.addMapping(initial_state, move_two_cannibals, two_cannibals_over)
    successor_fn.addMapping(initial_state, move_one_and_one, one_and_one_over)
    successor_fn.addMapping(initial_state, move_one_cannibal, one_cannibal_over)
    
    #be careful w/mappings that result in the initial_state
    #you could descend in an infinte loop...
    
    #Beginning in (two_cannibals_over)
    successor_fn.addMapping(two_cannibals_over, move_two_cannibals, initial_state)
    successor_fn.addMapping(two_cannibals_over, move_one_cannibal, one_cannibal_over_without_boat)
    
    #Beginning in (one_and_one_over)
    successor_fn.addMapping(one_and_one_over, move_one_and_one, initial_state)
    successor_fn.addMapping(one_and_one_over, move_one_missionary, one_cannibal_over_without_boat)
    
    #Beginning in (one_cannibal_over)
    successor_fn.addMapping(one_cannibal_over, move_one_cannibal, initial_state)
    
    #Beginning in (one_cannibal_over_without_boat)
    successor_fn.addMapping(one_cannibal_over_without_boat, move_one_cannibal, two_cannibals_over)
    successor_fn.addMapping(one_cannibal_over_without_boat, move_one_missionary, one_and_one_over)
    successor_fn.addMapping(one_cannibal_over_without_boat, move_two_cannibals, three_cannibals_over)
    
    #Beginning in (three_cannibals_over)
    successor_fn.addMapping(three_cannibals_over, move_one_cannibal, two_cannibals_over_without_boat)
    successor_fn.addMapping(three_cannibals_over, move_two_cannibals, one_cannibal_over_without_boat)
    
    #Beginning in (two_cannibals_over_without_boat)
    successor_fn.addMapping(two_cannibals_over_without_boat, move_two_missionaries, two_and_two_over)
    successor_fn.addMapping(two_cannibals_over_without_boat, move_one_cannibal, three_cannibals_over)
    
    #Beginning in (two_and_two_over)
    successor_fn.addMapping(two_and_two_over, move_two_missionaries, two_cannibals_over_without_boat)
    successor_fn.addMapping(two_and_two_over, move_one_and_one, one_and_one_over_without_boat)
    
    #Beginning in (one_and_one_over_without_boat)
    successor_fn.addMapping(one_and_one_over_without_boat, move_one_and_one, two_and_two_over)
    successor_fn.addMapping(one_and_one_over_without_boat, move_two_missionaries, three_missionaries_one_cannibal_over)
    
    #Beginning in (three_missionaries_one_cannibal_over)
    successor_fn.addMapping(three_missionaries_one_cannibal_over, move_two_missionaries, one_and_one_over_without_boat)
    successor_fn.addMapping(three_missionaries_one_cannibal_over, move_one_cannibal, three_missionaries_over_without_boat)
    
    #Beginning in (three_missionaries_over_without_boat)
    successor_fn.addMapping(three_missionaries_over_without_boat, move_one_cannibal, three_missionaries_one_cannibal_over)
    successor_fn.addMapping(three_missionaries_over_without_boat, move_two_cannibals, three_missionaries_two_cannibals_over)
    
    #Beginning in (three_missionaries_two_cannibals_over)
    successor_fn.addMapping(three_missionaries_two_cannibals_over, move_two_cannibals, three_missionaries_over_without_boat)
    successor_fn.addMapping(three_missionaries_two_cannibals_over, move_one_cannibal, three_missionaries_one_cannibal_over_without_boat)
    successor_fn.addMapping(three_missionaries_two_cannibals_over, move_one_missionary, two_and_two_over_without_boat)
    
    #Beginning in (two_and_two_over_without_boat)
    successor_fn.addMapping(two_and_two_over_without_boat, move_one_missionary, three_missionaries_one_cannibal_over)
    successor_fn.addMapping(two_and_two_over_without_boat, move_one_and_one, goal_state)
    
    #Beginning in (three_missionaries_one_cannibal_over_without_boat)
    successor_fn.addMapping(three_missionaries_one_cannibal_over_without_boat, move_one_cannibal, three_missionaries_two_cannibals_over)
    successor_fn.addMapping(three_missionaries_one_cannibal_over_without_boat, move_two_cannibals, goal_state)
    
    
    #Define the Search Problem
    missionaries_and_cannibals = SearchProblem(initial_state, successor_fn, goal_state)
    plan = tree_search(missionaries_and_cannibals)
    
    print(missionaries_and_cannibals)
    print("\nSolution: \n")
    for plan_step in plan:
        print(plan_step)
        
    
    
    
    
    
    
    
                            
    
    
    
    pass

if __name__ == '__main__':
    main()