def merging(arr, low, mid, high):
    count = 0
    j = mid + 1

    # Count valid pairs before merging
    for i in range(low, mid + 1):
        while j <= high and arr[i] > 2 * arr[j]:
            j += 1
        count += (j - (mid + 1))

    # Merge step (standard merge sort)
    temp = []
    left, right = low, mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return count


# Function to perform merge sort and count pairs
def mergeSort(arr, low, high):
    if low >= high:
        return 0

    mid = low + (high - low) // 2
    count = (mergeSort(arr, low, mid) +
             mergeSort(arr, mid + 1, high) +
             merging(arr, low, mid, high))

    return count


# Function to count reverse pairs
def countRevPairs(arr):
    return mergeSort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [3, 2, 4, 5, 1, 20]

    print(countRevPairs(arr))