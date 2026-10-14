"""Test of the solution for the DPV Algorithms book chapter 6 exercise 4."""

import unittest

from solutions.dpv_ch6_ex4 import solve
from tests.helpers import TestCase, run_test_cases


test_cases = [
    TestCase(
        inputs={
            "s": "itwasthebestoftimes",
            "is_word": lambda w: w in set(["it", "was", "the", "best", "of", "times"]),
        },
        expected="it was the best of times",
    ),
    TestCase(
        inputs={
            "s": "itwasthebestoftimes",
            "is_word": lambda w: w in set(["it", "was", "the", "best", "of"]),
        },
        expected="",
    ),
    TestCase(
        inputs={
            "s": "abcde",
            "is_word": lambda w: w in set(["a", "b", "c", "d", "cd", "cde"]),
        },
        expected="a b cde",
    ),
]


class TestSolution(unittest.TestCase):
    """Run the solution and verify the result of each test case."""

    def test_solution(self):
        """Run the solution and verify the result of each test case."""

        run_test_cases(test_cases, solve)
