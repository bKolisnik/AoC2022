import unittest
from Rucksack import rucksack, rucksack2
import os

class TestRucksack(unittest.TestCase):
    def test_rucksack(self):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "example.txt")
        with open(TESTDATA_FILENAME) as file:
            sacks = [line.rstrip() for line in file]
            count = rucksack(sacks)
            expected = 157
        self.assertEqual(count, expected)

    def test_rucksack2(self):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "example.txt")
        with open(TESTDATA_FILENAME) as file:
            sacks = [line.rstrip() for line in file]
            count = rucksack2(sacks)
            expected = 70
        self.assertEqual(count, expected)
