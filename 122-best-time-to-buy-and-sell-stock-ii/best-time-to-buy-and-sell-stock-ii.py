class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len1=len(prices)
        start=prices[0]
        max=0
        for i in range(0,len1):
            if start<prices[i]:
                max+=prices[i]-start
            start=prices[i]
        return max