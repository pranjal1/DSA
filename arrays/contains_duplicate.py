from typing import List


def contains_duplicate(nums: List[int]):
    dct = {}
    for n in nums:
        if dct.get(n):
            return True
        else:
            dct[n] = 1
    return False


print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
