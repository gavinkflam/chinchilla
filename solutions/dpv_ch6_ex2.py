"""Solution for the DPV Algorithms book chapter 6 exercise 2.

# Edge cases

1. n == 1
2. No penalties are needed

# Solutions

1. Brute force, backtracking
    - O(2^n) time, O(n) auxiliary space
2. DP / memo
    - O(n^2) time, O(n) auxiliary space
"""

import math


def solve(nums: list[int]) -> int:
    """Solve the problem."""

    n = len(nums)
    dp = [0]

    for hi in range(1, n):
        min_penalty = math.inf

        for lo in range(hi):
            penalty = dp[lo] + (200 - (nums[hi] - nums[lo])) ** 2
            min_penalty = min(min_penalty, penalty)

        dp.append(min_penalty)

    return dp[-1]
