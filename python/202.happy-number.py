#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            digits = [int(d) for d in str(n)]
            n = sum(x**2 for x in digits)
            
        return n == 1
        
# @lc code=end

