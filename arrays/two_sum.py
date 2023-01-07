from typing import List
from collections import defaultdict


def two_sum(nums: List[int], target: int):
    dct = defaultdict(list)
    for i in range(len(nums)):
        dct[nums[i]].append(i)

    diffs = [target - x for x in nums]

    for i in range(len(nums)):
        candidates = []
        if dct.get(diffs[i]):
            candidates = [x for x in dct.get(diffs[i]) if i != x]
        if candidates:
            return [i, candidates[0]]


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
