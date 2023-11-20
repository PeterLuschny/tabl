import unittest
from fractions import Fraction as frac
from NumBernoulli import Bernoulli

class TestBernoulli(unittest.TestCase):
    def test_bernoulli_zero(self):
        self.assertEqual(Bernoulli(0), frac(1, 1))

    def test_bernoulli_positive_odd(self):
        self.assertEqual(Bernoulli(1), frac(1, 2))
        self.assertEqual(Bernoulli(3), frac(0, 1))
        self.assertEqual(Bernoulli(5), frac(0, 1))
        # Add more tests for positive odd input values

    def test_bernoulli_positive_even(self):
        self.assertEqual(Bernoulli(2), frac(1, 6))
        self.assertEqual(Bernoulli(4), frac(-1, 30))
        self.assertEqual(Bernoulli(6), frac(1, 42))
        # Add more tests for positive even input values

if __name__ == '__main__':
    unittest.main()
