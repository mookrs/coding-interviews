def print_1_to_max_of_n_digits(n):
    if n <= 0:
        return

    number = ['0'] * n
    while not increment(number):
        print_number(number)


def increment(number):
    is_overflow = False
    take_over = 0
    length = len(number)

    for i in range(length - 1, -1, -1):
        sum_ = int(number[i]) + take_over
        if i == length - 1:
            sum_ += 1

        if sum_ >= 10:
            if i == 0:
                is_overflow = True
            else:
                sum_ -= 10
                take_over = 1
                number[i] = str(sum_)
        else:
            number[i] = str(sum_)
            break

    return is_overflow


def print_number(number):
    is_beginning_0 = True

    for i in range(len(number)):
        if is_beginning_0 and number[i] != '0':
            is_beginning_0 = False
        if not is_beginning_0:
            print('%c' % number[i], end='')
    print()


def print_1_to_max_of_n_digits_2(n):
    if n <= 0:
        return

    number = ['0'] * n
    for i in range(10):
        number[0] = str(i)
        print_1_to_max_of_n_digits_recursively(number, n, 0)


def print_1_to_max_of_n_digits_recursively(number, length, index):
    if index == length - 1:
        print_number(number)
        return
    for i in range(10):
        number[index + 1] = str(i)
        print_1_to_max_of_n_digits_recursively(number, length, index + 1)


print_1_to_max_of_n_digits(2)
print_1_to_max_of_n_digits_2(2)
