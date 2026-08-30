#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = []
        carry = 0
        while l1 is not None and l2 is not None:
            sum.append((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            
        while l1 is not None:
            sum.append((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            
        while l2 is not None:
            sum.append((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
        if carry > 0:
            sum.append(carry)
        head = ListNode(sum[0])
        curr = head 
        for val in sum[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head
# @lc code=end

