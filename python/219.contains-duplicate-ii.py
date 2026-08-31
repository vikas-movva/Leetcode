#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def hash_set():
            dupes = {}
            for i, num in enumerate(nums):
                if num in dupes and abs(dupes[num] - i) <= k:
                    return True
                dupes[num] = i
            return False
# @lc code=end
