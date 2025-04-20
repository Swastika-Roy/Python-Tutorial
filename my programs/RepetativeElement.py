class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

# Take user input
if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    solution = Solution()
    duplicate = solution.findDuplicate(arr)
    if duplicate != -1:
        print(f"The duplicate number is: {duplicate}")
    else:
        print("No duplicates found.")