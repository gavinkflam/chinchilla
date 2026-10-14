"""Test of the solution for the DPV Algorithms book chapter 6 exercise 2."""

import unittest

from solutions import dpv_ch6_ex2


test_cases = [
    {
        "input": [0, 50, 100, 200, 300, 401],
        "expected": 1,
    },
    {
        "input": [0, 100, 250, 300, 400],
        "expected": 5000,
    },
    {
        "input": [0],
        "expected": 0,
    },
    {
        "input": [0, 200],
        "expected": 0,
    },
]


class TestSolution(unittest.TestCase):
    """Run solution and verify the output of each test case."""

    def test_solution(self):
        """Run solution and verify the output of each test case."""

        for i, tc in enumerate(test_cases):
            actual = dpv_ch6_ex2.run(tc["input"])

            assert (
                actual == tc["expected"]
            ), f"test case #{i}: expected {tc['expected']}, got {actual}, input {tc['input']}"
