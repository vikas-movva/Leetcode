#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dp():
            max_p = 0
            l_buy = prices[0]
            
            for sell_p in prices:
                max_p = max(max_p, sell_p - l_buy)
                l_buy = min(sell_p, l_buy)
            return max_p
        
        def two_pointer():
            max_p, lp, rp = 0, 0, 1
            
            while rp < len(prices):
                profit = prices[rp] - prices[lp]
                if profit >=0:
                    max_p = max(max_p, profit)
                else:
                    lp = rp
                rp += 1
            
            return max_p
        
        return dp()
# @lc code=end

