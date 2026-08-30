#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for num in nums:
            if num in dups:
                return True
            dups.add(num)
        return False
        
# @lc code=end

