# 使用 dict 计数的方法会更简单一些
def more_than_half_Number(numbers):
    if not numbers:
        return 0

    result = numbers[0]
    count = 1
    for i in range(1, len(numbers)):
        if count == 0:
            result = numbers[i]
            count = 1
        elif numbers[i] != result:
            count -= 1
        else:
            count += 1

    return result if check_more_than_half(numbers, result) else 0


def check_more_than_half(numbers, result):
    count = 0
    for number in numbers:
        if number == result:
            count += 1

    return True if count * 2 > len(numbers) else False


print(more_than_half_Number([1, 3, 3, 2, 2, 2, 5, 4, 2]))
print(more_than_half_Number([1, 2, 3, 2, 2, 2, 5, 4, 2]))
