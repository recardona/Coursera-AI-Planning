'''
Created on Feb 16, 2013

@author: recardon
'''
import unittest
from state import State
from action import Action
from successor import SuccessorFunction

class Test(unittest.TestCase):

    def setUp(self):
        self.firstState  = State("First")
        self.secondState = State("Second")
        self.thirdState  = State("Third")
        self.fourthState = State("Fourth")
        self.firstAction = Action("<Action One>")
        self.secondAction = Action("<Action Two>")
        
        self.successorFunction = SuccessorFunction()
        self.successorFunction.addMapping(self.firstState, self.firstAction, self.secondState)
        self.successorFunction.addMapping(self.firstState, self.secondAction, self.thirdState)
        pass

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
        print(simpleFunctionString)


        print("--------------------------------------------\n")
        print("Trying to execute:\naddMapping((State First with conditions: (None)) ->\n\t(Action <Action One>, State Second with conditions: (None)))\n")
        print("This is a duplicate of the first mapping in a Successor Function and should not be reflected at all.\n")
        simpleFunction.addMapping(self.firstState, self.firstAction, self.secondState)
        simpleFunctionDupString = str(simpleFunction)
        print(simpleFunctionDupString)
        self.assertEqual(simpleFunctionString, simpleFunctionDupString, "Duplicate mappings in a Successor Function should not be reflected at all.")
        
        
        print("--------------------------------------------\n")
        print("Trying to execute:\naddMapping((State First with conditions: (None)) ->\n\t(Action <Action One>, State Third with conditions: (None)))\n")
        print("Applying the same action in the same state should not be allowed to result in two different states.\n")
        print("Adding this mapping should replace the original mapping.\n")
        simpleFunction.addMapping(self.firstState, self.firstAction, self.thirdState)
        simpleFunctionReplaceString = str(simpleFunction)
        print(simpleFunctionReplaceString)
        self.assertNotEqual(simpleFunctionString, simpleFunctionReplaceString, "Mapping one State to one Action with multiple resulting States keeps only the last-most State.")
        
                
    def testGettingApplicableActionsForStates(self):
        pass
        
    
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStateNameEquality', 'Test.testStateConditionsEquality', 'Test.testSuccessorFunctionDefinition']
    unittest.main()