import unittest
from RockPaperScissors import RockPaperScissors, RockPaperScissors2

class TestCalorieCounting(unittest.TestCase):
    def test_calorie_counting(self):
        count = RockPaperScissors([["A","Y"],["B","X"],["C","Z"]])
        expected = 15
        self.assertEqual(count, expected)
    def test_calorie_counting(self):
        count = RockPaperScissors2([["A","Y"],["B","X"],["C","Z"]])
        expected = 12
        self.assertEqual(count, expected)