class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        def getArea(i,j):
            nonlocal area
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 0:
                return area
            grid[i][j] = 0
            area += 1
            getArea(i + 1,j)
            getArea(i - 1,j)
            getArea(i,j + 1)
            getArea(i,j - 1)
            return area


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 0
                    area = getArea(i,j)
                    max_area = max(max_area, area)
        

        return max_area
