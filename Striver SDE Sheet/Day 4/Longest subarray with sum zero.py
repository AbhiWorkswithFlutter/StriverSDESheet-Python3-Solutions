#Question Link: https://takeuforward.org/data-structure/length-of-the-longest-subarray-with-zero-sum/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=ca2daf0acca561574693bd799573c265&pid=700254&user=tiabhi1999

class Solution:
    def maxLen(self, n, arr):
        maxlen = 0
        s = 0
        positions = {}
        for i in range(n):
            s+=arr[i]
            
            if s==0:
                maxlen = i + 1
            
            else:
                if positions.get(s) is not None:
                    maxlen = max(maxlen, i - positions[s])
                else:
                    positions[s] = i
        return maxlen
    

if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
