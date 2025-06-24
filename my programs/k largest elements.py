# Python program to find the k largest elements in the array
# using partitioning step of quick sort

# Function to partition the array around a pivot
def partition(arr, left, right):
    # Last element is chosen as a pivot.
    pivot = arr[right]
    i = left

    for j in range(left, right):

        # Elements greater than or equal to pivot
        # are placed in the left side of pivot
        if arr[j] >= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    # The correct sorted position of the pivot
    return i


def quickSelect(arr, left, right, k):
    if left <= right:
        pivotIdx = partition(arr, left, right)

        # Count of all elements in the left part
        leftCnt = pivotIdx - left + 1

        # If leftCnt is equal to k, then we have
        # found the k largest element
        if leftCnt == k:
            return

        # Search in the left subarray
        if leftCnt > k:
            quickSelect(arr, left, pivotIdx - 1, k)

        # Reduce the k by number of elements already covered
        # and search in the right subarray
        else:
            quickSelect(arr, pivotIdx + 1, right, k - leftCnt)


def kLargest(arr, k):
    quickSelect(arr, 0, len(arr) - 1, k)

    # First k elements of the array, will be the largest
    res = arr[:k]

    # Sort the result in descending order
    res.sort(reverse=True)
    return res


if __name__ == "__main__":
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    res = kLargest(arr, k)
    print(" ".join(map(str, res)))