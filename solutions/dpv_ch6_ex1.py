"""Solution for the DPV Algorithms book chapter 6 exercise 1.

# Edge cases

1. n == 1
2. nums[i] < 0
3. Answer involves negative numbers
4. All numbers are negative

# Solutions

1. Brute force, try each substring
    - O(n^2) time, O(1) auxiliary space
2. DP
    - O(n) time, O(n) auxiliary space
3. Greedy
    - O(n) time, O(1) auxiliary space
"""


def run(nums: list[int]) -> int:
    """Run the solution."""
    max_sum, current_sum = nums[0], 0

    for num in nums:
        current_sum = max(current_sum, 0) + num
        max_sum = max(max_sum, current_sum)

    return max_sum
