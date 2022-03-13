class Solution:
    def numIslands(self, grid):
        if grid is None or grid[0] is None:
            return 0
        rowlen = len(grid)
        collen = len(grid[0])
        res = 0
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j] == "1":
                    res += 1
                    self.bfs(grid, i, j, rowlen, collen)
        return res

    def bfs(self, grid, row, col, rowlen, collen):
        queue = []
        queue.append((row, col))
        grid[row][col] = "-1"

        while len(queue) > 0:
            points = queue.pop(0)
            i, j = points[0], points[1]
            #范围需要再进行一遍validation,因为存在+1，-1的情况，有越界的风险
            # left(i,j-1)
            if i >= 0 and i < rowlen and j-1 >= 0 and j-1 < collen and grid[i][j-1] == "1":
                queue.append((i, j - 1))
                grid[i][j-1] = "-1"
            #right(i,j+1)
            if i >= 0 and i < rowlen and j+1 >= 0 and j+1 < collen and grid[i][j+1] == "1":
                queue.append((i, j+1))
                grid[i][j+1] = "-1"
            # up (i-1,j)
            if i-1 >= 0 and i-1 < rowlen and j >= 0 and j < collen and grid[i-1][j] == "1":
                queue.append((i-1, j))
                grid[i-1][j] = "-1"
            # bottom
            if i + 1 >= 0 and i + 1 < rowlen and j >= 0 and j < collen and grid[i+1][j] == "1":
                queue.append((i+1, j))
                grid[i+1][j] = "-1"
        print(grid)

s = Solution()
res = s.numIslands([["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]])
print(res)