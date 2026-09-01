#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp, rp = 1, max(piles)
        while lp < rp:
            mid = (lp + rp)//2
            if sum((p +mid -1)//mid for p in piles) > h:
                lp = mid + 1
            else:
                rp = mid
        return lp

# @lc code=end

