import pytest
from fib import fibonacci, factorial

class TestFib:

    def test_fib_vals(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(5) == 5


class Testfactorialtorial:

    def test_factorialtorial_vals(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120