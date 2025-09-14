# best time to buy and sell the stock

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    p=0
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            buy=prices[i]
            sell=prices[j]
            if buy<sell:
                p=sell-buy
    print(p,sell,buy)
maxProfit([7,1,5,3,6,4])