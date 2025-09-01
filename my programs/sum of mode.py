from collections import defaultdict
import bisect

def sumOfModes(arr, k):
    n = len(arr)
    sum = 0

    # Stores frequency of elements
    # in current window
    mp = defaultdict(int)

    # Stores (frequency, -value) to maintain
    # order of mode selection
    st = []

    # Build frequency map for the first window
    for i in range(k):
        mp[arr[i]] += 1

    # Populate the set with initial frequency pairs
    for key, val in mp.items():
        bisect.insort(st, (val, -key))

    # Add mode of the first window
    mode = -st[-1][1]
    sum += mode

    # Slide the window across the array
    for i in range(k, n):
        out = arr[i - k]
        in_ = arr[i]

        # Remove the outgoing element's
        # previous frequency pair
        outFreq = mp[out]
        st.remove((outFreq, -out))

        # Decrement frequency of
        # outgoing element
        mp[out] -= 1

        # If frequency is still positive,
        # reinsert updated pair
        if mp[out] > 0:
            bisect.insort(st, (mp[out], -out))
        else:
            del mp[out]

        # Increment frequency of incoming element
        mp[in_] += 1

        # Insert updated frequency pair
        # for incoming element
        bisect.insort(st, (mp[in_], -in_))

        # Get current mode and add to sum
        mode = -st[-1][1]
        sum += mode

    return sum

if __name__ == "__main__":
    arr = [1, 2, 3, 2, 5, 2, 4, 4]
    k = 3

    result = sumOfModes(arr, k)
    print(result)