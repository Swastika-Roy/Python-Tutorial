import heapq

def minSoldiers(arr, k):
    n = len(arr)
    need = (n + 1) // 2
    lucky = 0

    # Min-heap for storing costs to make a troop lucky
    pq = []

    for num in arr:
        if num % k == 0:
            lucky += 1
        else:
            heapq.heappush(pq, k - (num % k))

    # If already enough lucky troops, cost is 0
    if lucky >= need:
        return 0

    total = 0
    required = need - lucky

    # Take smallest `required` costs from heap
    for _ in range(required):
        if pq:
            total += heapq.heappop(pq)

    return total

if __name__ == "__main__":
    arr = [3, 5, 6, 7, 9, 11]
    k = 4
    print(minSoldiers(arr, k))