class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def primeList(head):
    current = head
    while current:
        current.val = nearestPrime(current.val)
        current = current.next
    return head

def nearestPrime(num):
    if isPrime(num):
        return num

    lower = num - 1
    upper = num + 1

    while True:
        lowerPrime = lower >= 2 and isPrime(lower)
        upperPrime = isPrime(upper)

        if lowerPrime and upperPrime:
            return lower
        if lowerPrime:
            return lower
        if upperPrime:
            return upper

        lower -= 1
        upper += 1

def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
