class Solution:
    def maxProfit(self, prices):
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]  # our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit

    def maxProfit2(self, prices):
        leftBuy, rightSell = 0, 1
        maxP = 0
        #不能越界
        while rightSell < len(prices):
            #profitable?
            if prices[leftBuy] < prices[rightSell]:
                profit = prices[rightSell] - prices[leftBuy]
                maxP = max(maxP,profit)
            else:
                # 为了找更低的买入点，当 price [rightSell] < prices[leftBuy] 
                # 说明rightsell的数字更小,就把right的指针指向left
                #之前不用换因为没有比这个小的
                leftBuy = rightSell
            rightSell += 1

        return maxP

    # def maxProfit3(self, prices):

so = Solution()
mp = so.maxProfit2(prices=[2,1,3,4,1,5,1,7])
print(mp)                

