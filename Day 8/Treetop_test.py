import unittest
from Treetop import treetop
import os

class TestRucksack(unittest.TestCase):
    def test_rucksack(self):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "example.txt")
        with open(TESTDATA_FILENAME) as file:
            sacks = [line.rstrip() for line in file]
            count = treetop(sacks)
            expected = 157
        self.assertEqual(count, expected)