#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # find middle of list
        sp = fp = head
        
        while fp.next and fp.next.next:
            sp = sp.next
            fp = fp.next.next
            
        # sp is now middle
        # reverse second half of list 
        # and cut off sp
        prev, curr, sp.next = None, sp.next, None
        while curr:
            next, curr.next, prev = curr.next, prev, curr
            curr = next
        
        # merge two lists
        l1, l2 = head, prev
        while l2:
            n1, n2 = l1.next, l2.next
            l1.next = l2
            l2.next = n1
            l1, l2 = n1, n2
            
# @lc code=end
    