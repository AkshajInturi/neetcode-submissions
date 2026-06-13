class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = len(prices)-1
        i=0
        max_profit = 0
        while i < len(prices)-1:
            running_min = prices[i]
            j = i+1
            while j < len(prices):
                prof = prices[j]-prices[i]
                if prof > max_profit:
                    max_profit = prof
                j+=1
            i+=1
        return max_profit