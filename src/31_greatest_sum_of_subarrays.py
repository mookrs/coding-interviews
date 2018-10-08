def find_greatest_sum_of_subarray(array):
    cur_sum = 0
    max_sum = float('-inf')

    for i in array:
        if cur_sum <= 0:
            cur_sum = i
        else:
            cur_sum += i

        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum


print(find_greatest_sum_of_subarray([6, -3, -2, 7, -15, 1, 2, 2]))
