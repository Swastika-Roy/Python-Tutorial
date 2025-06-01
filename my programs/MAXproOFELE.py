class Solution:
    def maxProduct(self, nums):
        smax = -1
        max_val = -1
        for num in nums:
            if max_val < num:
                smax = max_val
                max_val = num
            elif smax < num:
                smax = num
        return (max_val - 1) * (smax - 1)
