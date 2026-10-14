"""Test of the solution for the DPV Algorithms book chapter 6 exercise 1."""

import unittest

from solutions.dpv_ch6_ex1 import solve
from tests.helpers import TestCase, run_test_cases


test_cases = [
    TestCase(
        inputs={
            "nums": [5, 15, 10],
        },
        expected=30,
    ),
    TestCase(
        inputs={
            "nums": [5, 15, -30, 10, -5, 40, 10],
        },
        expected=55,
    ),
    TestCase(
        inputs={
            "nums": [-5, -15, -30, -10, -5, -40, -10],
        },
        expected=-5,
    ),
    TestCase(
        inputs={
            "nums": [5],
        },
        expected=5,
    ),
]


class TestSolution(unittest.TestCase):
    """Run the solution and verify the result of each test case."""

    def test_solution(self):
        """Run the solution and verify the result of each test case."""

        run_test_cases(test_cases, solve)
