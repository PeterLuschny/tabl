import unittest
from NumBell import bell_num


class TestBellNum(unittest.TestCase):
    def test_bell_num_zero(self):
        self.assertEqual(bell_num(0), 1)

    def test_bell_num_positive(self):
        self.assertEqual(bell_num(1), 1)
        self.assertEqual(bell_num(2), 2)
        self.assertEqual(bell_num(3), 5)
        self.assertEqual(bell_num(4), 15)
        self.assertEqual(bell_num(5), 52)
        # Add more tests for positive input values

if __name__ == '__main__':
    unittest.main()
