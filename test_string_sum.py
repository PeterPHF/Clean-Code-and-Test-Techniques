import unittest
from sum_integers import sum_integers_in_string

class TestSumIntegers(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sum_integers_in_string("1a2b3"), 6)

    def test_multiple_digits(self):
        self.assertEqual(sum_integers_in_string("abc12xyz3"), 15)

    def test_no_numbers(self):
        self.assertEqual(sum_integers_in_string("abc"), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_integers_in_string("100test20"), 120)

if __name__ == "__main__":
    unittest.main()