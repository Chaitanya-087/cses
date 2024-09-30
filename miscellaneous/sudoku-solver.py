from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(row, col, num):
            s_row, s_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(9):
                if board[i][col] == num or board[row][i] == num or board[s_row + i // 3][s_col + i % 3] == num: return False
            return True
        
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in "123456789":
                            if isValid(i,j,num):
                                board[i][j] = num
                                if solve(): return True
                                board[i][j] = "."
                        return False
            return True
              
        solve()

solution = Solution()

board = [["5",".",".",".","7",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
solution.solveSudoku(board)
print(board)
