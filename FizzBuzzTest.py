import unittest
from FizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def setUp (self):
        self.fiBuzzCalculator = FizzBuzz()
    def testReturNumber (self):
        self.assertEqual(1, self.fiBuzzCalculator.getValue(1))
    def testCheckFizz (self):
        self.assertEqual("Fizz", self.fiBuzzCalculator.getValue(3))
    def testCheckBuzz (self):
        self.assertEqual("Buzz", self.fiBuzzCalculator.getValue(5))
    def testCheckFizzBuzz (self):
        self.assertEqual("FizzBuzz", self.fiBuzzCalculator.getValue(15))
    def testCheckfrom1to15 (self):
        fizz_buzz_dict = {1:1,2:2,3:"Fizz",4:4,5:"Buzz",6:"Fizz",7:7,8:8,9:"Fizz",10:"Buzz",11:11,12:"Fizz",13:13,14:14,15:"FizzBuzz"}
        for number in range (1,16):
            self.assertEqual(fizz_buzz_dict.get(number), self.fiBuzzCalculator.getValue(number))

if __name__ == '__main__':
    unittest.main()
