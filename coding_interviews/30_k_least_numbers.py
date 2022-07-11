import heapq


def get_least_k_nums1(nums, k):
    if not nums or len(nums) < k or k <= 0:
        return []

    return heapq.nsmallest(k, nums)


def get_least_k_nums2(nums, k):
    if not nums or len(nums) < k or k <= 0:
        return []

    output = []

    for elem in nums:
        elem = -elem
        if len(output) < k:
            heapq.heappush(output, elem)
        else:
            least = output[0]
            if elem > least:
                heapq.heapreplace(output, elem)

    return sorted([-x for x in output])


print(get_least_k_nums1([4, 5, 1, 6, 2, 7, 3, 8], 4))
print(get_least_k_nums2([4, 5, 1, 6, 2, 7, 3, 8], 4))
