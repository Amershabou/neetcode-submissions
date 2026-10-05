class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        pairs = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for row in board:
            r = [i for i in row if i != "."]
            if len(r) != len(set(r)):
                return False
        
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
                
        for row, col in pairs:
            seen = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        return True
