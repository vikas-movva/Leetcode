#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(10)]
        cols = [set() for _ in range(10)]
        grid = [set() for _ in range(10)]
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if board[i][j] == ".": continue
                
                grid_idx = (j // 3) + ((i // 3) * 3)
                if cell in rows[i] or cell in cols[j] or cell in grid[grid_idx]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grid[grid_idx].add(board[i][j])
                
        return True
# @lc code=end