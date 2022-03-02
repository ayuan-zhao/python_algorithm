# -*- coding: utf-8 -*-
class Solution:
    def maxProfit(self, prices):
        buy = 0
        sell = 1#sell起码要和buy隔一天
        maxprofit = 0
        #先决条件：不能越界
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                currentprofit = prices[sell]-prices[buy]
                maxprofit = max(maxprofit, currentprofit)
            else:
                buy = sell
            #left不要随便加，没找到更低的点就在这待着
            sell += 1
        return maxprofit


so = Solution()
mp = so.maxProfit(prices=[2, 1,3,4,1,5,1,7])
print(mp)
