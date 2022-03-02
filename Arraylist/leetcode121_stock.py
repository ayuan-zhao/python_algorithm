class Solution:
    def maxProfit(self, prices):
        left = 0  # Buy
        right = 1  ##sell起码要和buy隔一天
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] 
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
                #left不要随便加，没找到更低的点就在这待着
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
            #left不要随便加，没找到更低的点就在这待着
            rightSell += 1
        #永远注意return位置
        return maxP

    # def maxProfit3(self, prices):

so = Solution()
mp = so.maxProfit2(prices=[2,1,3,4,1,5,1,7])
print(mp)                

