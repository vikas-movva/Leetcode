/*
 * @lc app=leetcode id=136 lang=rust
 *
 * [136] Single Number
 */

use crate::Solution;
// @lc code=start
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut result = 0;
        for num in nums{
            result = result ^ num;
        }
        result
    }
}
// @lc code=end

