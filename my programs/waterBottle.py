class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            newBottles = emptyBottles // numExchange
            totalBottles += newBottles
            emptyBottles = newBottles + (emptyBottles % numExchange)
        return totalBottles