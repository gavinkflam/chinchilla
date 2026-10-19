"""Solution for the DPV Algorithms book chapter 6 exercise 11.

# Edge cases

1. n == 1 and/or m == 1
2. m != n
3. x == y
4. No common subsequences

# Solutions

1. Brute force, backtracking
    - O(2^(m + n)) time, O(m + n) auxiliary space
2. DP / memo
    - O(mn) time, O(mn) auxiliary space
3. DP, optimized space
    - O(mn) time, O(min(m, n)) auxiliary space
"""


def solve(x: str, y: str) -> int:
    """Solve the problem."""

    # Use the shorter string as x to improve space complexity
    if len(y) < len(x):
        x, y = y, x

    # DP
    n, m = len(x), len(y)
    dp1 = [0] * (m + 1)

    for i in range(n):
        dp0 = [0] * (m + 1)

        for j in range(m):
            if x[i] == y[j]:
                dp0[j] = dp1[j - 1] + 1
            else:
                dp0[j] = max(dp0[j - 1], dp1[j])

        dp1 = dp0

    return dp1[m - 1]
