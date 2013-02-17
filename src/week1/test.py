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
        self.firstToSecondAction = Action("<Action One>")
        self.thirdToFourthAction = Action("<Action Two>")
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
        simpleFunction.addMapping(self.firstState, self.firstToSecondAction, self.secondState)
        simpleFunction.addMapping(self.thirdState, self.thirdToFourthAction, self.fourthState)
        print(simpleFunction)

        print("Trying to execute: addMapping((State First with conditions: (None)) ->\n\t(Action <Action One>, State Second with conditions: (None)))\n")
        print("This is a duplicate of the first mapping in a Successor Function and should not be reflected at all.")
        
        simpleFunction.addMapping(self.firstState, self.firstToSecondAction, self.secondState)
        self.assertEqual(len(simpleFunction), 2, "A repeated function mapping should not contribute more size")
        
        # Adding a different firstState mapping!
        simpleFunction.addMapping(self.firstState, self.firstToSecondAction, self.thirdState)
        
        print(simpleFunction)
        
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStateNameEquality', 'Test.testSuccessorFunctionDefinition']
    unittest.main()