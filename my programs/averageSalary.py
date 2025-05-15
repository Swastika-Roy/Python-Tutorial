def avg_salary(arr):
    if len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements.")

    min_val = arr[0]
    max_val = arr[0]
    total = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
        total += arr[i]

    total -= min_val + max_val
    average = total / (len(arr) - 2)  # Use float division for precision

    return average

# Example usage
arr = [100, 200, 300, 400]
print(avg_salary(arr))  # Output: 250.0
