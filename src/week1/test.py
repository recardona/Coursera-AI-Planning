'''
Created on Feb 16, 2013

@author: recardon
'''
import unittest
from state import State
from action import Action
from successor import SuccessorFunction
from search import SearchNode
from search import SearchProblem


class Test(unittest.TestCase):

    def setUp(self):
        self.firstState  = State("First")
        self.secondState = State("Second")
        self.thirdState  = State("Third")
        self.fourthState = State("Fourth")
        self.firstAction = Action("<Action One>")
        self.secondAction = Action("<Action Two>")
        self.thirdAction  = Action("<Action Three>")
        
        self.successorFunction = SuccessorFunction()
        self.successorFunction.addMapping(self.firstState, self.firstAction, self.firstState)
        self.successorFunction.addMapping(self.firstState, self.secondAction, self.secondState)
        
        self.searchProblem = SearchProblem(self.firstState, self.successorFunction, self.secondState)
        

    def tearDown(self):
        pass

    def testStateNameEquality(self):
        left    = State("Left")
        leftToo = State("Left")
        right   = State("Right")
        
        self.assertEqual(left, leftToo, "States should be equal")
        self.assertNotEqual(left, right, "States should not be equal")
    
    def testStateConditionsEquality(self):
        allLeft    = State("AllLeft", {'L':{'3m','3c','b'}, 'R':{'0m','0c'}})
        allLeftToo = State("AllLeft", {'L':{'3m','3c','b'}, 'R':{'0m','0c'}})
        allRight   = State("AllRight", {'L':{'0m','0c'}, 'R':{'3m','3c','b'}})
        
        self.assertEqual(allLeft, allLeftToo, "These two States have identical names and conditions")
        self.assertNotEqual(allLeft, allRight, "These two States have different names and conditions")
        
    def testSuccessorFunctionDefinition(self):
        simpleFunction = SuccessorFunction()
        simpleFunction.addMapping(self.firstState, self.firstAction, self.secondState)
        simpleFunctionString = str(simpleFunction)
        #Verbose output:
#        print(simpleFunctionString)
        
 
#        print("--------------------------------------------\n")
#        print("Trying to execute:\naddMapping((State First with conditions: (None)) ->\n\t(Action <Action One>, State Second with conditions: (None)))\n")
#        print("This is a duplicate of the first mapping in a Successor Function and should not be reflected at all.\n")
        simpleFunction.addMapping(self.firstState, self.firstAction, self.secondState)
        simpleFunctionDupString = str(simpleFunction)
#        print(simpleFunctionDupString)
        self.assertEqual(simpleFunctionString, simpleFunctionDupString, "Duplicate mappings in a Successor Function should not be reflected at all.")
                
#        print("--------------------------------------------\n")
#        print("Trying to execute:\naddMapping((State First with conditions: (None)) ->\n\t(Action <Action One>, State Third with conditions: (None)))\n")
#        print("Applying the same action in the same state should not be allowed to result in two different states.\n")
#        print("Adding this mapping should replace the original mapping.\n")
        simpleFunction.addMapping(self.firstState, self.firstAction, self.thirdState)
        simpleFunctionReplaceString = str(simpleFunction)
        print(simpleFunctionReplaceString)
        self.assertNotEqual(simpleFunctionString, simpleFunctionReplaceString, "Mapping one State to one Action with multiple resulting States keeps only the last-most State.")
        
    def testGettingApplicableActionsForStates(self):
        applicable_actions = self.successorFunction.getApplicableActionsInState(self.firstState)
        self.assertTrue(type(applicable_actions)==type(set()), "The returned value should be a Set")
        
        for action in applicable_actions:
            print(type(action))
            self.assertTrue(type(action)==Action, "Each element of the Set should be an Action")
        
        self.assertIn(self.firstAction, applicable_actions, "<Action One> should be in the returned Set")
        self.assertNotIn(self.thirdAction, applicable_actions, "<Action Three> should not be in the returned Set")
        
    def testResolveActionInState(self):
        resulting_state = self.successorFunction.resolveActionInState(self.firstState, self.firstAction)
        self.assertTrue(type(resulting_state)==State, "Resulting state should be a State")
        self.assertEqual(resulting_state, self.firstState, "Correct State is returned for applying corresponding Action")
        self.assertIsNone(self.successorFunction.resolveActionInState(self.thirdState, self.firstAction), "If State is not mapped, resulting State is None")
        self.assertIsNone(self.successorFunction.resolveActionInState(self.firstState, self.thirdAction), "If State is not mapped to given Action, resulting State is None")
        
    def testGoalTest(self):
        secondStateNode = SearchNode(self.secondState)
        self.assertTrue(self.searchProblem.goalTest(secondStateNode), "The SearchNode for the second State is the goal of this toy Search Problem")
        self.assertFalse(self.searchProblem.goalTest(self.secondState), "The Second State should be the goal of this toy Search Problem, but we're passing in a State, not a Node")
        self.assertFalse(self.searchProblem.goalTest(self.firstState), "The First State should not be the goal of this toy Search Problem")
        self.assertFalse(self.searchProblem.goalTest(1), "A number is not a State!  This should be False")
        

            
    
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStateNameEquality', 'Test.testStateConditionsEquality', 'Test.testSuccessorFunctionDefinition', 'Test.testGettingApplicableActionsForStates', 'Test.testResolveActionInState', 'Test.testGoalTest']
    unittest.main()