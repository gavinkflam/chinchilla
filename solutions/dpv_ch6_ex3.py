"""Solution for the DPV Algorithms book chapter 6 exercise 3.

# Edge cases

1. n == 1
2. Can select all the locations

# Solutions

1. Brute force, backtracking
    - O(2^n) time, O(n) auxiliary space
2. DP / memo
    - O(n^2) time, O(n) auxiliary space
3. DP, two pointers
    - O(n) time, O(n) auxiliary space
"""


def solve(locations: list[int], profits: list[int], k: int) -> int:
    """Solve the problem."""

    n = len(locations)
    dp = [0] * (n + 1)
    dp[0], lo = profits[0], -1

    for hi in range(1, n):
        while lo + 1 < hi and locations[hi] - locations[lo + 1] >= k:
            lo += 1

        dp[hi] = max(dp[hi - 1], dp[lo] + profits[hi])

    return dp[n - 1]
