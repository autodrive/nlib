import unittest

import nlib


class TestNLib(unittest.TestCase):
    def test_fib(self):
        result0 = nlib.fib(0)
        expected0 = 0
        self.assertEqual(expected0, result0)

        result1 = nlib.fib(1)
        expected1 = 1
        self.assertEqual(expected1, result1)

        result2 = nlib.fib(2)
        expected2 = 1
        self.assertEqual(expected2, result2)

        result10 = nlib.fib(10)
        expected10 = 55
        self.assertEqual(expected10, result10)


if __name__ == '__main__':
    unittest.main()
