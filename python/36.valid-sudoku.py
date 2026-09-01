#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def hash_set() -> bool:
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
        
        def bitmask() -> bool:
            rows = [0 for _ in range(9)] 
            cols = [0 for _ in range(9)]
            grid = [0 for _ in range(9)]
            
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        continue 
                    cell = (1 << (int(board[i][j]) - 1))
                    if cell & rows[i] or cell & cols[j] or cell & grid[(i//3) * 3 + j // 3]:
                        return False
                    
                    rows[i] |= cell
                    cols[j] |= cell
                    grid[(i//3) * 3 + j // 3] |= cell
                    
            return True
        
        # return hash_set() # hash set solution
        return bitmask() # bitmask solution
# @lc code=end