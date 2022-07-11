def power(base, exponent):
    if equal_zero(base) and exponent < 0:
        raise ZeroDivisionError

    ret = power_value(base, abs(exponent))
    if exponent < 0:
        return 1 / ret
    else:
        return ret


def equal_zero(num):
    if abs(num - 0.0) < 0.0000001:
        return True


def power_value(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    ret = power_value(base, exponent >> 1)
    ret *= ret
    if exponent & 1 == 1:
        ret *= base
    return ret


print(power(2, 8))
print(power(2, 9))
