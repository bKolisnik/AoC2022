import unittest
from CalorieCounting import calorie_counting, calorie_counting2

class TestCalorieCounting(unittest.TestCase):
    def test_calorie_counting(self):
        count = calorie_counting(['1000','2000','3000','','4000','','5000','6000','','7000','8000','9000','','10000',''])
        expected = 24000
        self.assertEqual(count, expected)

    def test_calorie_counting2(self):
        count = calorie_counting2(['1000','2000','3000','','4000','','5000','6000','','7000','8000','9000','','10000',''])
        expected = 24000+11000+10000
        self.assertEqual(count, expected)