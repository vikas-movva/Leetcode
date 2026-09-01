#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".": continue
                
                grid_idx = (j // 3) + ((i // 3) * 3)
                if cell in rows[i] or cell in cols[j] or cell in grid[grid_idx]:
                    return False
                rows[i].add(cell)
                cols[j].add(cell)
                grid[grid_idx].add(cell)
                
        return True
# @lc code=end