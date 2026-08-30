#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        p1 = 0
        longest = 0
        
        for p2 in range(len(s)):
            count[s[p2]] = count.get(s[p2], 0) + 1
            
            while (p2 - p1 + 1) - max(count.values()) > k:
                count[s[p1]] -= 1
                p1 += 1
            
            longest = max(longest, p2 - p1 + 1)
        
        return longest
# @lc code=end

