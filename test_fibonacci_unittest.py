import unittest
from fib import fibonacci, factorial

class test_fibonacci(unittest.TestCase):

    def test_fib_vals(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)

class test_factorial(unittest.TestCase):

    def test_fac_vals(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()
        
