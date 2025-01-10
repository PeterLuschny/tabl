import unittest
from TernaryTrees import ternarytrees

class TestTernaryTree(unittest.TestCase):
    def test_ternarytree_zero(self):
        self.assertEqual(ternarytrees(0), [1])

    def test_ternarytree_one(self):
        self.assertEqual(ternarytrees(1), [0, 1])

    def test_ternarytree_two(self):
        self.assertEqual(ternarytrees(2), [0, 1, 3])

    def test_ternarytree_three(self):
        self.assertEqual(ternarytrees(3), [0, 1, 5, 12])

    def test_ternarytree_four(self):
        self.assertEqual(ternarytrees(4), [0, 1, 7, 25, 55])

    # Add more tests for other values of n

if __name__ == '__main__':
    unittest.main()
