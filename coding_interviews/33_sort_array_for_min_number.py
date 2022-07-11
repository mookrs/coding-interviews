import functools


def print_min_number(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=functools.cmp_to_key(cmp_func))
    return ''.join(numbers_str)


def cmp_func(a, b):
    if a + b > b + a:
        return 1
    elif a + b < b + a:
        return -1
    else:
        return 0


print(print_min_number([3, 5, 1, 4, 2]))
