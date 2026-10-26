# Unit testing with unittest

import unittest

# Functions to test
def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

# Test class
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    def test_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

# Running the tests
if __name__ == "__main__":
    unittest.main(exit=False)
