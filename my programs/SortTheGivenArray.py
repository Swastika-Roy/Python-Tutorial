from typing import List

def sort_array(arr: List[int], A: int, B: int, C: int) -> List[int]:
    def evaluate(x: int) -> int:
        return A * x * x + B * x + C

    # Apply the transformation and sort
    transformed = [evaluate(x) for x in arr]
    transformed.sort()

    return transformed
