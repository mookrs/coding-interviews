def reorder(nums, func):
    left, right = 0, len(nums) - 1
    while left < right:
        while left < right and not func(nums[left]):
            left += 1
        while left < right and func(nums[right]):
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]


def is_even(num):
    return (num & 1) == 0


tests = [2, 3, 4, 5, 6, 7]
reorder(tests, is_even)
print(tests)
