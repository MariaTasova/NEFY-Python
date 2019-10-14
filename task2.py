def get_sorted_squares(nums):
    square = []
    for i in range(len(nums)):
        nums[i] = nums[i]**2
        square.append(nums[i])
        for k in range(len(square) - 1):
            for j in range(len(square) - 1):
                if square[j] > square[j + 1]:
                    square[j], square[j + 1] = square[j + 1], square[j]
    return square


nums = [4,-1,0,3,10]
print(get_sorted_squares(nums))


