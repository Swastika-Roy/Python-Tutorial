class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    # Calculate value-to-weight ratio
    def get_ratio(self):
        return self.value / self.weight


def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.get_ratio(), reverse=True)

    max_value = 0.0

    for item in items:
        if capacity >= item.weight:
            # If the item can fit completely, add its full value
            max_value += item.value
            capacity -= item.weight
        else:
            # If the item can't fit completely, take the fraction that fits
            max_value += item.get_ratio() * capacity
            break  # Knapsack is full

    return max_value


# Example usage
if __name__ == "__main__":
    items = [
        Item(10, 60),  # Weight = 10, Value = 60
        Item(20, 100),  # Weight = 20, Value = 100
        Item(30, 120)  # Weight = 30, Value = 120
    ]

    capacity = 50
    max_value = fractional_knapsack(items, capacity)
    print(f"Maximum value in Knapsack = {max_value}")
