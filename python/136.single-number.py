#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A function that returns the length of the value:
        # ans = 0
        # for num in nums:
        #     ans = ans ^ num
        
        # return ans
        seen = {}
        
        for n in nums:
            if n not in seen:
                seen[n] = True
            else:
                del seen[n]
                
        return next(iter(seen.keys()))
        
# @lc code=end

