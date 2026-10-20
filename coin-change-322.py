'''
Day 11
2 attempts
'''
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        noOfWays: list[int | None] = [None for i in range(0,amount+1)]
        noOfWays[0] = 0
        def findWays(amount) -> int:
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if noOfWays[amount] is not None:
                return noOfWays[amount]
            minWays = amount + 1
            for coin in coins:
                if coin <= amount:
                    remainderMinWays = findWays(amount - coin)
                    if remainderMinWays != -1:
                        minWays = min(minWays, 1 + remainderMinWays)
            noOfWays[amount] = minWays if minWays < amount + 1 else -1
            return noOfWays[amount]
        
        return findWays(amount)
        