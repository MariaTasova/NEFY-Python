def get_two_sum(*nums, target):
    nums = list(nums)
    for i in range(0, len(nums)-1):
        for k in range(i+1, len(nums)):
            if nums[i] + nums[k] == target:
                return i, k
    return "None"

print(get_two_sum(2, 8, 7, 11, 4, 5, 5, 4, 8, 15, 1, target=15))
