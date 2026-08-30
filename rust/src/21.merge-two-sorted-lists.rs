/*
 * @lc app=leetcode id=21 lang=rust
 *
 * [21] Merge Two Sorted Lists
 */

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

use crate::Solution;

// @lc code=start
impl Solution {
    pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = ListNode::new(0);
        let mut current = &mut dummy;

        while let (Some( n1), Some(n2)) = (&list1, &list2) {
            if n1.val <= n2.val {
                if let Some(mut node) = list1 {
                    list1 = node.next.take();
                    current.next = Some(node);
                }
            } else {
                if let Some(mut node) = list2 {
                    list2 = node.next.take();
                    current.next = Some(node);
                }
            }
            current = current.next.as_mut().unwrap();
        }

        current.next = if list1.is_some() { list1 } else { list2 };
        dummy.next
    }
}
// @lc code=end

