"""Test of the solution for the DPV Algorithms book chapter 6 exercise 1."""

import unittest

from solutions import dpv_ch6_ex1


test_cases = [
    {
        "input": [5, 15, 10],
        "expected": 30,
    },
    {
        "input": [5, 15, -30, 10, -5, 40, 10],
        "expected": 55,
    },
    {
        "input": [-5, -15, -30, -10, -5, -40, -10],
        "expected": -5,
    },
    {
        "input": [5],
        "expected": 5,
    },
]


class TestSolution(unittest.TestCase):
    """Run solution and verify the output of each test case."""

    def test_solution(self):
        """Run solution and verify the output of each test case."""

        for i, tc in enumerate(test_cases):
            actual = dpv_ch6_ex1.run(tc["input"])

            assert (
                actual == tc["expected"]
            ), f"test case #{i}: expected {tc['expected']}, got {actual}, input {tc['input']}"
