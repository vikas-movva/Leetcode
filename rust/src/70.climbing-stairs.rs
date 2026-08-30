/*
 * @lc app=leetcode id=70 lang=rust
 *
 * [70] Climbing Stairs
 */

use crate::Solution;

// @lc code=start
#[warn(dead_code)]
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n == 1{
            1 as i32
        }else if n == 2{
            2 as i32
        }else{
            let mut dp = vec![0; n as usize +1];
            dp[1 as usize] = 1;
            dp[2 as usize] = 2;
            for i in 3..n+1{
                dp[i as usize] = dp[(i-1) as usize] + dp[(i-2) as usize]
            }
            dp[n as usize] as i32
        }
    }
}
// @lc code=end

