import heapq

def median(mat):
    rows = len(mat)
    cols = len(mat[0])

    # min-heap storing [value, row, col]
    minHeap = []
    medianIndex = (rows * cols) // 2
    count = 0
    result = -1

    # push the first element of each row into
    # the min-heap
    for i in range(rows):
        heapq.heappush(minHeap, [mat[i][0], i, 0])

    # extract the smallest elements until reaching
    # the median
    while count <= medianIndex:
        val, row, col = heapq.heappop(minHeap)
        result = val
        count += 1

        # if more elements are left in the current
        # row, push next
        if col + 1 < cols:
            heapq.heappush(minHeap, \
              [mat[row][col + 1], row, col + 1])

    return result

if __name__ == "__main__":
    matrix = [
        [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]
    ]
    print(median(matrix))