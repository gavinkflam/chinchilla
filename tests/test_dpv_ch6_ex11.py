"""Test of the solution for the DPV Algorithms book chapter 6 exercise 11."""

import unittest

from solutions.dpv_ch6_ex11 import solve
from tests.helpers import TestCase, run_test_cases


test_cases = [
    TestCase(
        inputs={
            "x": "tobeornottobe",
            "y": "ithinkthereforeiam",
        },
        expected=5,
    ),
    TestCase(
        inputs={
            "x": "moomoo",
            "y": "moomoo",
        },
        expected=6,
    ),
    TestCase(
        inputs={
            "x": "m",
            "y": "moomoo",
        },
        expected=1,
    ),
    TestCase(
        inputs={
            "x": "moomoo",
            "y": "m",
        },
        expected=1,
    ),
    TestCase(
        inputs={
            "x": "m",
            "y": "m",
        },
        expected=1,
    ),
    TestCase(
        inputs={
            "x": "abcdefg",
            "y": "hijklmnop",
        },
        expected=0,
    ),
]


class TestSolution(unittest.TestCase):
    """Run the solution and verify the result of each test case."""

    def test_solution(self):
        """Run the solution and verify the result of each test case."""

        run_test_cases(test_cases, solve)
