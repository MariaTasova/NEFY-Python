def get_three_sum(nums, target):
    for i in range(0, len(nums)-2):
        for k in range(i+1, len(nums)-1):
            for j in range(k+1, len(nums)):
                if nums[i] + nums[k] + nums[j] == target:
                    return i, k, j
    return "None"

print(get_three_sum([2, 7, 11, 15], target=24))