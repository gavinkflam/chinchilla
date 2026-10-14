"""Solution for the DPV Algorithms book chapter 6 exercise 4.

# Edge cases

1. n == 1
2. No ways to reconstruct the string
    - Return an empty string
3. Multiple ways to reconstruct the string
    - Assume the answer is unique

# Solutions

1. Brute force, backtracking
    - O(2^n) time, O(n) auxiliary space
2. DP / memo
    - O(n^3) time, O(n) auxiliary space
        - O(n^2) is only possible in languages with constant time string slicing
"""

from typing import Callable


def solve(s: str, is_word: Callable[[str], bool]) -> str:
    """Solve the problem."""

    n = len(s)

    # At each index, find out is there a way to break s[0 : i + 1] into words
    dp = [0] * (n + 1)
    dp[-1] = 1

    for hi in range(n):
        for lo in range(-1, hi):
            if dp[lo] > 0 and is_word(s[lo + 1 : hi + 1]):
                dp[hi] = hi - lo
                break

    if dp[n - 1] == 0:
        return ""

    # Reconstruct the string
    ans = []
    i = n - 1

    while i >= 0:
        ans.append(s[i - dp[i] + 1 : i + 1])
        i -= dp[i]

    ans.reverse()
    return " ".join(ans)
