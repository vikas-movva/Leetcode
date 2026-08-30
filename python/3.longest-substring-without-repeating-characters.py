#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        seen = set()
        longest = 0 
        while p2 < len(s):
            if s[p2] not in seen:
                seen.add(s[p2])
                longest = max(longest, p2 - p1 + 1)
                p2 += 1
            else:
                seen.remove(s[p1])
                p1 += 1
        return longest
        
# @lc code=end

