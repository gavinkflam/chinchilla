"""Test of the solution for the DPV Algorithms book chapter 6 exercise 3."""

import unittest

from solutions import dpv_ch6_ex3


test_cases = [
    {
        "input": {
            "locations": [0, 50, 100, 200, 220, 240],
            "profits": [8, 10, 12, 16, 17, 9],
            "k": 100,
        },
        "expected": 37,
    },
    {
        "input": {
            "locations": [0, 50, 100, 200, 220, 240],
            "profits": [8, 10, 12, 16, 17, 9],
            "k": 1,
        },
        "expected": 72,
    },
    {
        "input": {
            "locations": [0],
            "profits": [10],
            "k": 100,
        },
        "expected": 10,
    },
]


class TestSolution(unittest.TestCase):
    """Run solution and verify the output of each test case."""

    def test_solution(self):
        """Run solution and verify the output of each test case."""

        for i, tc in enumerate(test_cases):
            actual = dpv_ch6_ex3.run(
                tc["input"]["locations"], tc["input"]["profits"], tc["input"]["k"]
            )

            assert (
                actual == tc["expected"]
            ), f"test case #{i}: expected {tc['expected']}, got {actual}, input {tc['input']}"
