import unittest
from Narayana import narayana

class TestNarayana(unittest.TestCase):
    def test_narayana_zero(self):
        self.assertEqual(narayana(0), [1])

    def test_narayana_one(self):
        self.assertEqual(narayana(1), [0, 1])

    def test_narayana_two(self):
        self.assertEqual(narayana(2), [0, 1, 1])

    def test_narayana_positive(self):
        self.assertEqual(narayana(3), [0, 1, 3, 1])
        self.assertEqual(narayana(4), [0, 1, 6, 6, 1])
        self.assertEqual(narayana(5), [0, 1, 10, 20, 10, 1])
        # Add more tests for positive input values

if __name__ == '__main__':
    unittest.main()