#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        sig = 1
        
        for i in range(1, n+1):
            if sig*2 == i:
                sig = i
            dp[i] = 1 + dp[i - sig]
            
        return dp
# @lc code=end

