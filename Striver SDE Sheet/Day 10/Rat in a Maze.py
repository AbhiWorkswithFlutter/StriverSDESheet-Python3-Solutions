#Question Link: https://takeuforward.org/data-structure/rat-in-a-maze/
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=01a7f634323f1ee67b6b434b96a6a3d0&pid=700408&user=tiabhi1999

#For complete question and code snippet, please refer the GFG link (https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1#)

class Solution:
    def dfs(self, i, j, m, n, visited, ans, s, dx, dy):
        if i == n-1 and j == n-1:
            ans.append(s)
            return
        
        dr = "DLRU"
        
        for ind in range(4):
            x = i +  dx[ind]
            y = j + dy[ind]
            if x >= 0 and x < n and y >= 0 and y < n and visited[x][y] != 1 and m[x][y] == 1:
                visited[i][j] = 1
                self.dfs(x, y, m, n, visited, ans, s+dr[ind], dx, dy)
                visited[i][j] = 0
    
    def findPath(self, m, n):
        ans = []
        visited = [ [0 for j in range(n)] for i in range(n) ]
        dx = [1, 0, 0, -1]
        dy = [0, -1, 1, 0]
        if m[0][0] == 1:
            self.dfs(0, 0, m, n, visited, ans, "", dx, dy)
      
        return ans
