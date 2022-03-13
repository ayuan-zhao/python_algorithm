class Solution:
    def numIslands0(self, grid) -> int:
        #grid 是横坐标row,grid[0]是纵坐标
        if grid is None or grid[0] is None:
            return 0
        rowLen,colLen,res = len(grid), len(grid[0]), 0
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == '1':
                    res += 1
                    self.bfs(grid, i, j, rowLen, colLen)
        return res
        #如果检测到grid[i][j]= 1，说明是 island,
    
    def bfs(self, grid, row :int, col:int, rowLen:int, colLen:int):
        queue = []
        queue.append((row, col))
        grid[row][col] = "-1"
        
        while len(queue) > 0:
            points = queue.pop(0)
            #i和j 是 pop出来的row的值和，col的值
            i, j = points[0], points[1]
            # left i,j-1
            if i>=0 and i<rowLen and j-1>=0 and j-1<colLen and "1"==grid[i][j-1]:
                queue.append((i, j-1))
                grid[i][j-1]="-1"
            #right i j+1
            if i>=0 and i<rowLen and j+1>=0 and j+1<colLen and "1"==grid[i][j+1]:
                queue.append((i, j+1))
                grid[i][j+1]="-1"
            # top i-1,j
            if i-1>=0 and i-1<rowLen and j>=0 and j<colLen and "1"==grid[i-1][j]:
                queue.append((i-1, j))
                grid[i-1][j]="-1"
            # bottom =i+1, j
            if i+1>=0 and i+1<rowLen and j>=0 and j<colLen and "1"==grid[i+1][j]:
                queue.append((i+1, j))
                grid[i+1][j]="-1"
    def numIslands1(self, grid) -> int:
        if not grid:
            return 0
        rowLen,colLen,res = len(grid), len(grid[0]), 0
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == '1':
                    res += 1
                    # print(i, j)
                    self.bfs(grid, i, j, rowLen, colLen)
        return res
    
    def bfs(self, grid, row :int, col:int, rowLen:int, colLen:int):
        queue = []
        queue.append((row, col))
        grid[row][col] = "-1"
        
        while len(queue) > 0:
            points = queue.pop(0)
            i, j = points[0], points[1]
            # for newi, newj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
            #     if newi>=0 and newi<rowLen and newj>=0 and newj<colLen and "1"==grid[newi][newj]:
            #         grid[newi][newj] = "-1"
            #         queue.append((newi, newj))
            for di, dj in (-1,0),(1,0),(0,-1),(0,1):
                newi,newj = i+di, j+dj
                if newi>=0 and newi<rowLen and newj>=0 and newj<colLen and "1"==grid[newi][newj]:
                    grid[newi][newj] = "-1"
                    queue.append((newi, newj))
                
        # print(grid)






    def numIslands3(self, grid) -> int:
        #input validation
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        # print("len(grid) ",len(grid),"len(grid[0]",len(grid[0])
        visit = set()
        islands = 0
#breath-first search is not a recursive algorithm,it's iterative
#a queue is normally used for bfs for memory                   
        def bfs(r,c): 
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
                  
# while q is not empty,we're gonna be expanding islands         
            while q:
                row,col = q.popleft()
              #check this just poped adjacent position
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r,c = row + dr,col +dc
                    if(r in range(rows) and 
                       c in range(cols) and
                       grid[r][c] =="1" and 
                       (r,c) not in visit):
                        q.append((r,c))
                       #set use add,list use append
                        visit.add((r,c))       
                       
            for r in range(rows):
                for c in range(cols):
                  #remeber grid made up of strings not numbers
                    if grid[r][c]== "1" and (r,c)not in visit:
                        bfs(r,c)
                        #new island increment
                        islands += 1
            return islands      
                  
        