class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = {}

        def rottenFruit(i,j, minute):
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != 1:
                return
            if f'{i},{j}' in seen:
                if minute >= seen[f'{i},{j}']:
                    return
            seen[f'{i},{j}'] = minute
            rottenFruit(i + 1,j, minute + 1)
            rottenFruit(i - 1,j, minute + 1)
            rottenFruit(i,j + 1, minute + 1)
            rottenFruit(i,j - 1, minute + 1)

        num_of_fresh = 0
        num_of_rotten = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    num_of_rotten += 1
                    rottenFruit(i + 1, j, 1)
                    rottenFruit(i - 1, j, 1)
                    rottenFruit(i, j + 1, 1)
                    rottenFruit(i, j - 1, 1)
                if grid[i][j] == 1:
                    num_of_fresh += 1
        
        if len(seen) < num_of_fresh:
            return -1
        if num_of_rotten == 0 or num_of_fresh == 0:
            return 0

        
        return max(list(seen.values())) if list(seen.values()) else -1

        