#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(31):
            r = (r << 1) | (n & 1)
            n >>= 1
        return r
# @lc code=end