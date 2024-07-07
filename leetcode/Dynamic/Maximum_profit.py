class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        low_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < low_price:
                low_price = price
            elif price -low_price > max_profit:
                max_profit = price - low_price
        
        return max_profit

       


prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))