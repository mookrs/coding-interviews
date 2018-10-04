def fib1(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b


def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b


for i in fib1(10):
    print(i)

print(fib2(10))
