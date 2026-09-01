#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Quickselect variant - Dutch national flag algorithm
        # divide the list with three pointers lp, pivot, rp
        def quickselect(left, right, largest_k):
            if left == right:
                return nums[left]
            
            pivot_i = random.randint(left, right)
            pivot = nums[pivot_i]
            
            lp = left
            i = left
            rp = right
            
            while i <= rp:
                if nums[i] < pivot:
                    nums[lp], nums[i] = nums[i], nums[lp]
                    lp += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[rp], nums[i] = nums[i], nums[rp]
                    rp -= 1 
                else:
                    i += 1
                    
            if largest_k < lp:
                return quickselect(left, lp - 1, largest_k)
            elif largest_k > rp:
                return quickselect(rp + 1, right, largest_k)
            else:
                return pivot
            
        return quickselect(0, n - 1, n - k)
        
        # quickselect is faster than heapq
        def heap():
            heapq.heapify(nums) 
            while len(nums) > k:
                heapq.heappop(nums)
            return nums[0]
    
        return heap() # Min-Heap solution
    
# @lc code=end