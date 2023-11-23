import unittest
from Motzkin import motzkin

class TestMotzkin(unittest.TestCase):
    def test_motzkin_zero(self):
        self.assertEqual(motzkin(0), [1])

    def test_motzkin_one(self):
        self.assertEqual(motzkin(1), [1, 0])

    def test_motzkin_two(self):
        self.assertEqual(motzkin(2), [1, 0, 1])

    def test_motzkin_three(self):
        self.assertEqual(motzkin(3), [1, 0, 3, 0])

    def test_motzkin_four(self):
        self.assertEqual(motzkin(4), [1, 0, 6, 0, 2])

    # Add more tests for other values of n

if __name__ == '__main__':
    unittest.main()
