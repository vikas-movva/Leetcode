#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        n = len(s)
        if s == "":
            return True
        
        
        for i in range(n//2):
            if s[i] != s[(n - 1) - i]:
                return False
        
        return True
# @lc code=end

