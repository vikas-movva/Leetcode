#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        ans = [0]
        sig = 1
        
        for i in range(1, n+1):
            if sig*2 == i:
                sig = i
        
            dp[i] = dp[i-sig]+1
            ans.append(dp[i])
         
        return ans
# @lc code=end

