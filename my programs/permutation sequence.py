def getPermutation(self, n: int, k: int) -> str:
        import math
        numbers = [i for i in range(1, n + 1)]
        fact = math.factorial(n - 1)
        k -= 1  # Convert to 0-based index
        ans = ''

        while numbers:
            index = k // fact
            ans += str(numbers[index])
            numbers.pop(index)
            if not numbers:
                break
            k %= fact
            fact //= len(numbers)

        return ans
