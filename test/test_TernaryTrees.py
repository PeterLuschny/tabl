import unittest
from TernaryTrees import ternarytree

class TestTernaryTree(unittest.TestCase):
    def test_ternarytree_zero(self):
        self.assertEqual(ternarytree(0), [1])

    def test_ternarytree_one(self):
        self.assertEqual(ternarytree(1), [0, 1])

    def test_ternarytree_two(self):
        self.assertEqual(ternarytree(2), [0, 1, 3])

    def test_ternarytree_three(self):
        self.assertEqual(ternarytree(3), [0, 1, 5, 12])

    def test_ternarytree_four(self):
        self.assertEqual(ternarytree(4), [0, 1, 7, 25, 55])

    # Add more tests for other values of n

if __name__ == '__main__':
    unittest.main()
