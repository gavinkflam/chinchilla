"""Test of the solution for the DPV Algorithms book chapter 6 exercise 2."""

import unittest

from solutions.dpv_ch6_ex2 import solve
from tests.helpers import TestCase, run_test_cases


test_cases = [
    TestCase(
        inputs={
            "nums": [0, 50, 100, 200, 300, 401],
        },
        expected=1,
    ),
    TestCase(
        inputs={
            "nums": [0, 100, 250, 300, 400],
        },
        expected=5000,
    ),
    TestCase(
        inputs={
            "nums": [0],
        },
        expected=0,
    ),
    TestCase(
        inputs={
            "nums": [0, 200],
        },
        expected=0,
    ),
]


class TestSolution(unittest.TestCase):
    """Run the solution and verify the result of each test case."""

    def test_solution(self):
        """Run the solution and verify the result of each test case."""

        run_test_cases(test_cases, solve)
