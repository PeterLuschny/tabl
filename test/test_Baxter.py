import unittest
from Baxter import baxter

class TestBaxter(unittest.TestCase):
    def test_baxter_zero(self):
        self.assertEqual(baxter(0), [1])

    def test_baxter_positive(self):
        self.assertEqual(baxter(1), [0, 1])
        self.assertEqual(baxter(2), [0, 1, 1])
        self.assertEqual(baxter(3), [0, 1, 4, 1])
        self.assertEqual(baxter(4), [0, 1, 10, 10, 1])
        # Add more tests for positive input values

if __name__ == '__main__':
    unittest.main()