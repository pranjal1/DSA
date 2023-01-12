import random


def selection_sort(arr):
    for i in range(len(arr)):
        min_val = arr[i]
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_idx = j
        tmp = arr[min_idx]
        arr[min_idx] = arr[i]
        arr[i] = min_val
    return arr


for _ in range(5):
    arr = [random.randint(0, 100) for _ in range(10)]
    print(arr)
    print(selection_sort(arr))
    print("----------")
