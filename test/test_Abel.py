import unittest
from Abel import abel

class TestAbel(unittest.TestCase):
    def test_abel_zero(self):
        self.assertEqual(abel(0), [1])

    def test_abel_positive(self):
        self.assertEqual(abel(1), [0, 1])
        self.assertEqual(abel(2), [0, 2, 1])
        self.assertEqual(abel(3), [0, 9, 6, 1])
        self.assertEqual(abel(4), [0, 64, 48, 12, 1])
        # Weitere Tests für positive Eingabewerte

if __name__ == '__main__':
    unittest.main()
