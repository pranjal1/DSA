def fib_helper(n, n1, n2, idx):
    sum_so_far = n1 + n2
    if sum_so_far == n:
        return idx
    if sum_so_far > n:
        return -1
    n1 = n2
    n2 = sum_so_far
    idx += 1
    return fib_helper(n, n1, n2, idx)


def find_fib_index(n):
    assert n >= 0
    if n <= 1:
        print(f"index of {n} = ", n)
        return
    res = fib_helper(n, 0, 1, 3)
    if res == -1:
        print(f"{n} is not a fibonacci number!")
    else:
        print(f"index of {n} = ", res)


find_fib_index(5)
find_fib_index(8)
find_fib_index(21)
find_fib_index(0)
find_fib_index(1)
find_fib_index(4)
find_fib_index(10)
find_fib_index(4181)


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
