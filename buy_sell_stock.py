class Solution:
    def maxProfit(self, prices: [int]) ->int:
        l,r = 0,1
        maxP = 0

        while r< len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP
p1 = Solution()
print(p1.maxProfit([7,1,5,3,6,4]))