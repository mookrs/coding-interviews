def number_of_1(n):
    count = 0
    while n:
        count += 1
        n = n & (n - 1)
    return count


def power_of_2(n):
    if n & (n - 1) == 0:
        return True
    else:
        return False


def m_to_n_change_time(m, n):
    diff = m ^ n
    count = 0
    while diff:
        count += 1
        diff = diff & (diff - 1)
    return count


print(number_of_1(66))
print(power_of_2(64), power_of_2(63))
print(m_to_n_change_time(66, 63))
