nums = [1, 2, 3, 4, 5]
target = 6
 # Output: [0, 4] or [1, 3] (depending on iteration order)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]  # Return immediately when found
    return []  # This line is theoretically unreachable given the problem constraints
print(twoSum(nums, target))