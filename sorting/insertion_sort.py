# list is almost sorted, in this case insertion sort is very useful. I think this is a stable sort

import random


def insertion_sort(arr):
    len_arr = len(arr)
    if len_arr < 2:
        return arr

    for i in range(1, len_arr):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


for _ in range(5):
    arr = [random.randint(0, 100) for _ in range(10)]
    print(arr)
    print(insertion_sort(arr))
    print("----------")
