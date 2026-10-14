"""Test of the solution for the DPV Algorithms book chapter 6 exercise 3."""

import unittest

from solutions.dpv_ch6_ex3 import solve
from tests.helpers import TestCase, run_test_cases


test_cases = [
    TestCase(
        inputs={
            "locations": [0, 50, 100, 200, 220, 240],
            "profits": [8, 10, 12, 16, 17, 9],
            "k": 100,
        },
        expected=37,
    ),
    TestCase(
        inputs={
            "locations": [0, 50, 100, 200, 220, 240],
            "profits": [8, 10, 12, 16, 17, 9],
            "k": 1,
        },
        expected=72,
    ),
    TestCase(
        inputs={
            "locations": [0],
            "profits": [10],
            "k": 100,
        },
        expected=10,
    ),
]


class TestSolution(unittest.TestCase):
    """Run the solution and verify the result of each test case."""

    def test_solution(self):
        """Run the solution and verify the result of each test case."""

        run_test_cases(test_cases, solve)
