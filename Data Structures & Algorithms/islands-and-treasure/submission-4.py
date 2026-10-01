from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (
                    ni < 0 or ni >= rows or
                    nj < 0 or nj >= cols
                ):
                    continue

                if grid[ni][nj] < 2147483647:
                    continue

                if grid[ni][nj] < grid[i][j]:
                    continue

                grid[ni][nj] = grid[i][j] + 1

                queue.append((ni, nj))