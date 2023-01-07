from typing import List


def rotate(nums: List[int], k: int):
    new_arr = []
    len_arr = len(nums)
    for i in range(len_arr):
        idx = i - k
        if idx < 0:
            idx = len_arr + idx
        new_arr.append(nums[idx])

    return new_arr


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate([-1, -100, 3, 99], 2))
