class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                prof = prices[j] - prices[i]
                if prof > maxP:
                    maxP = prof

        if (maxP == 0):
            return 0

        return maxP