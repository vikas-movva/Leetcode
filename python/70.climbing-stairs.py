#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [0] * (n + 1)

        for i in range(1, n+1):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else: 
                dp[i] = dp[i-2] + dp[i-1]

        return dp[n]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(1))  # Output: 1
    print(solution.climbStairs(2))  # Output: 2
    print(solution.climbStairs(3))  # Output: 3
    print(solution.climbStairs(4))  # Output: 5
    print(solution.climbStairs(5))  # Output: 8