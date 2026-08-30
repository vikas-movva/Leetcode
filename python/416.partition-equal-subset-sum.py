#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n_sum = sum(nums)
        if  n_sum % 2:
            return False
        
        nums.sort()
        
        n = len(nums)
        lp = 0
        rp = 0
        left_sum = 0
        right_sum = 0
        for i in range(0, len(nums)):
            if left_sum + nums[i] < n_sum /2: 
                left_sum += nums[i]
                
            if right_sum + nums[(n-1)-i] < n_sum /2: 
                right_sum += nums[(n-1)-i]
            
        
        return lp == rp - 1
        
# @lc code=end

