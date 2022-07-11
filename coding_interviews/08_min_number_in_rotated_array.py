def min_num_in_torated_array(numbers):
    if not numbers:
        return

    index1, index2 = 0, len(numbers) - 1
    index_mid = index1
    while numbers[index1] >= numbers[index2]:
        if index2 - index1 == 1:
            index_mid = index2
            break

        index_mid = (index1 + index2) // 2
        if numbers[index1] == numbers[index_mid] == numbers[index2]:
            return min_in_order(numbers, index1, index2)

        if numbers[index_mid] >= numbers[index1]:
            index1 = index_mid
        elif numbers[index_mid] <= numbers[index2]:
            index2 = index_mid

    return numbers[index_mid]


def min_in_order(numbers, index1, index2):
    result = numbers[index1]
    for i in numbers[index1 + 1:index2 + 1]:
        if result > numbers[i]:
            result = numbers[i]
    return result


print(min_num_in_torated_array([3, 4, 5, 1, 2]))
print(min_num_in_torated_array([1, 2, 3, 4, 5]))
print(min_num_in_torated_array([1, 0, 1, 1, 1]))
print(min_num_in_torated_array([]))
