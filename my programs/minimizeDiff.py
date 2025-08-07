# Convert "HH:MM:SS" to total seconds since midnight
def toSeconds(time: str) -> int:
    h = int(time[0:2])
    m = int(time[3:5])
    s = int(time[6:8])

    return h * 3600 + m * 60 + s


def minDifference(arr: list[str]) -> int:
    totalSec = 24 * 3600

    # Boolean array to mark seen
    # seconds size = 86400
    seen = [False] * totalSec

    n = len(arr)

    # Mark all seconds in the seen
    # array, return 0 on duplicate
    for i in range(n):
        sec = toSeconds(arr[i])
        if seen[sec]:
            return 0
        seen[sec] = True

    first = -1
    last = -1
    prev = -1
    minDiff = float('inf')

    # finding minimum difference
    # between adjacent times
    for i in range(totalSec):
        if not seen[i]:
            continue
        if prev != -1:
            minDiff = min(minDiff, i - prev)
        else:
            first = i
        prev = i
        last = i

    # wrap-around difference
    # between last and first
    wrap = first + totalSec - last
    minDiff = min(minDiff, wrap)

    return minDiff


if __name__ == "__main__":
    arr = ["12:30:15", "12:30:45"]
    result = minDifference(arr)
    print(result)