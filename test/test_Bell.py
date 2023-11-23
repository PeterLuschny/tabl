import unittest
from Bell import bell


class TestBell(unittest.TestCase):
    def test_bell_zero(self):
        self.assertEqual(bell(0), [1])

    def test_bell_positive(self):
        self.assertEqual(bell(1), [1, 2])
        self.assertEqual(bell(2), [2, 3, 5])
        self.assertEqual(bell(3), [5, 7, 10, 15])
        self.assertEqual(bell(4), [15, 20, 27, 37, 52])
        # Add more tests for positive input values


if __name__ == '__main__':
    unittest.main()
