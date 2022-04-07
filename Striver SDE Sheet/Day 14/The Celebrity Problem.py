#Question Link: https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1
#Solution (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=a35b3892529a0d7e17b56ad4cbce16f9&pid=700253&user=tiabhi1999

#For complete question and code snippet, please refer the GFG link (https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1)

class Solution:
    
    def celebrity(self, M, n):
        arr = []
        for i in range(n):
            arr.append(i)
        while(len(arr)>=2):
            a = arr.pop()
            b = arr.pop()
            if(M[a][b] == 1):
                arr.append(b)
            else:
                arr.append(a)
        if len(arr) <1:
            return -1
        x = arr.pop()
        
        for i in range(n):
            if i != x:
                if(M[i][x] == 0 or M[x][i] == 1):
                    return -1
        return x
