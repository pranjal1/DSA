def fib(counter, n1, n2):
    if counter == 0:
        return
    counter -= 1
    sum_term = n1 + n2
    print(sum_term, end=", ")
    n1 = n2
    n2 = sum_term
    fib(counter, n1, n2)


def fibonacci(n):
    assert n > 0
    if n == 1:
        print(0)
        return
    if n == 2:
        print(0, 1)
        return
    print(0, end=", ")
    print(1, end=", ")
    fib(n - 2, 0, 1)


# def fibonacci(n):
#     # print(n)
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n -2)


fibonacci(20)
