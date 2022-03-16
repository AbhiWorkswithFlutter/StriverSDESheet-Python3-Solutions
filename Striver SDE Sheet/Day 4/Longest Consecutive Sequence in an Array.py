#Question Link: https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=26aa19ce3d0edfa51f3b4ced7f370b3d&pid=701295&user=tiabhi1999

#For complete question and code snippet, please refer GFG link (https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1/#)

class Solution:
    
    def findLongestConseqSubseq(self,arr, N):
        if len(arr) < 1:
            return 0
        res = 0
        d = {}
        for i in range(N):
            if arr[i] not in d:
                d[arr[i]] = i
        
        for i in range(N):
            count = 0
            if arr[i] - 1 not in d:
                flag = True
                temp = arr[i]
                while(flag):
                    if temp in d:
                        count += 1
                        temp += 1
                    else:
                        flag = False
                res = max(res, count)
                
        return res
                
        
