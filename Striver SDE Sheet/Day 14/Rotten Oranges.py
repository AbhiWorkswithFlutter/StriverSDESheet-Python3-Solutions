#Question Link: https://takeuforward.org/data-structure/rotten-oranges-min-time-to-rot-all-oranges-bfs/
#Solution Link (Python 3): https://leetcode.com/submissions/detail/687325991/


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def rot(rotten):
            temp = []
            for i,j in rotten:
                if i > 0 and grid[i-1][j] == 1:
                    temp.append((i-1,j))
                    grid[i-1][j] = 2
                if i < row-1 and grid[i+1][j] == 1:
                    temp.append((i+1,j))
                    grid[i+1][j] = 2
                if j > 0 and grid[i][j-1] == 1:
                    temp.append((i,j-1))
                    grid[i][j-1] = 2
                if j < col-1 and grid[i][j+1] == 1:
                    temp.append((i,j+1))
                    grid[i][j+1] = 2
            return temp
        rotten = [(i,j) for i in range(row) for j in range(col) if grid[i][j] == 2]
        timereq = 0
        while rotten:
            rotten = rot(rotten)
            if len(rotten) == 0:
                break
            timereq+=1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return timereq
                    
        
        
            
        
