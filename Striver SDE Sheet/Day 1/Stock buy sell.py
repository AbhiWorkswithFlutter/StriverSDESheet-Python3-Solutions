#Question link: https://takeuforward.org/data-structure/stock-buy-and-sell/
#Solution Link (Python3): https://leetcode.com/submissions/detail/656604769/


class Solution:
    def maxProfit(self, prices):
        maxprofit = 0
        minprice = float("inf")
		
        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            maxprofit = max(maxprofit,prices[i]-minprice)
            
            
        return maxprofit

prices = list(map(int, input().split()))

ans = Solution().maxProfit(prices)

print(ans)
