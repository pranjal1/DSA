def first_recurring(nums):
    dct = {}
    for i in nums:
        if dct.get(i):
            return i
        else:
            dct[i] = 1
    return None


print(first_recurring([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring([2, 3, 4, 5]))
print(first_recurring([2, 1, 1, 2, 3, 5, 1, 2, 4]))
