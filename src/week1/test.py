'''
Created on Feb 16, 2013

@author: recardon
'''
import unittest
from state import State


class Test(unittest.TestCase):


    def testStateNameEquality(self):
        left    = State("Left")
        leftToo = State("Left")
        right   = State("Right")
        
        self.assertEqual(left, leftToo, "States should be equal")
        self.assertNotEqual(left, right, "States should not be equal")
    
    def testStateConditionsEquality(self):
        allLeft    = State("AllLeft", {'L':{'3m','3c','b'}, 'R':{'0m','0c'}});
        allLeftToo = State("AllLeft", {'L':{'3m','3c','b'}, 'R':{'0m','0c'}});
        allRight   = State("AllRight", {'L':{'0m','0c'}, 'R':{'3m','3c','b'}});
        
        self.assertEqual(allLeft, allLeftToo, "These two States have identical names and conditions")
        self.assertNotEqual(allLeft, allRight, "These two States have different names and conditions")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStateEquality']
    unittest.main()