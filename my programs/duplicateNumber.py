class Solution:
    def findDuplicate(self, nums):
        ans = 0

        for i in range(len(nums)):
            ele = abs(nums[i])
            if nums[ele] > 0:
                nums[ele] = -nums[ele]
            else:
                ans = ele
                break

        # Restore the array
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return ans
