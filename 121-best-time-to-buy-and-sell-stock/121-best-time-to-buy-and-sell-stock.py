class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        low = 1e+4
        profit = [0]
        
        for i in range(1, n):
            low = min(low, prices[i-1])
            profit.append(prices[i]-low)
                
        
        profit.sort(reverse=True)
        return profit[0]
        
        