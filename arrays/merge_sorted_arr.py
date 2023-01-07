import math


def merge_sorted_arrays(arr1, arr2):
    merged = []
    l1 = len(arr1)
    l2 = len(arr2)

    if l1 == 0:
        return arr2
    if l2 == 0:
        return arr1

    i, j = 0, 0
    for idx in range(l1 + l2):
        if i < l1:
            c1 = arr1[i]
        else:
            c1 = math.inf
        if j < l2:
            c2 = arr2[j]
        else:
            c2 = math.inf
        if c1 < c2:
            merged.append(c1)
            i += 1
        else:
            merged.append(c2)
            j += 1
    return merged


print(merge_sorted_arrays([1, 2], [3, 4]))
print(merge_sorted_arrays([0, 3, 4], [4, 6, 30]))
print(merge_sorted_arrays([1, 2, 5], [3, 4]))
