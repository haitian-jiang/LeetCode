def RadixSort(nums):
    """use 10 as the base for radix
    so the length of int in decimal becomes the time of iteration"""
    max_digit = max(map(len, map(str, nums)))
    radix = 1
    for d in range(max_digit):
        counter = [0] * 10
        partial_sorted = [0] * len(nums)
        for i in range(len(nums)):
            counter[nums[i]%(radix*10)//radix] += 1
        for i in range(1, len(counter)):
            counter[i] += counter[i - 1]
        for i in range(len(nums) - 1, -1, -1):
            partial_sorted[counter[nums[i]%(radix*10)//radix] - 1] = nums[i]  # index -1 because A and sorted_A starts from index 0
            counter[nums[i]%(radix*10)//radix] -= 1
        nums = partial_sorted
        radix *= 10
    return nums


if __name__ == '__main__':
    import random
    length = 1000
    A = list(range(length))
    random.shuffle(A)
    print(A)
    check = list(range(length))
    A = RadixSort(A)
    print(A)
    print(A == check)
