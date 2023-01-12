import random


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
    return arr


for _ in range(5):
    arr = [random.randint(0, 100) for _ in range(10)]
    print(arr)
    print(bubble_sort(arr))
    print("----------")
