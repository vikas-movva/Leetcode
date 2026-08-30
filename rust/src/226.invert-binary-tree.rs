/*
 * @lc app=leetcode id=226 lang=rust
 *
 * [226] Invert Binary Tree
 */


// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}
use crate::Solution;
// @lc code=start
use std::rc::Rc;
use std::cell::{Ref, RefCell};
#[allow(dead_code)]
impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = root.clone() {
            // Borrow the node mutably
            let mut node_borrow = node.borrow_mut();
            
            // Take ownership of the left and right children, replacing them with None
            let left = node_borrow.left.take();
            let right = node_borrow.right.take();
            
            // Recursively invert the subtrees and swap their positions
            node_borrow.left = Self::invert_tree(right);
            node_borrow.right = Self::invert_tree(left);
        }
        root
    }
}
// @lc code=end

