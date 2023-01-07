from math import inf
from typing import List


def max_subarray(nums: List[int]):
    max_so_far = -inf
    max_ending_here = 0

    for i in range(len(nums)):
        max_ending_here = max_ending_here + nums[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


print(max_subarray([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]))
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([1]))
print(max_subarray([5, 4, -1, 7, 8]))
