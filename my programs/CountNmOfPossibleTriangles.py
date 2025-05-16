class Solution:
    @staticmethod
    def countTriangles(arr):
        res = 0

        # Sort the array to apply the triangle inequality efficiently
        arr.sort()

        # Iterate through pairs of sides (arr[i], arr[j])
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):

                # Binary search for the first index where arr[k] >= arr[i] + arr[j]
                lo, hi = j + 1, len(arr)
                target = arr[i] + arr[j]
                while lo < hi:
                    mid = lo + (hi - lo) // 2
                    if arr[mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid

                # Count the number of valid third sides
                cnt = lo - j - 1
                res += cnt

        return res
