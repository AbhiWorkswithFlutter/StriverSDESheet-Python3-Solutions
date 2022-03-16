#Question Link: https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=b0dab7b4bc35fb23c11e22547b2b5604&pid=701241&user=tiabhi1999

#For Complete code snippet, please refer the GFG question link (https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1)

class Solution:
    
    def find3Numbers(self,A, n, X):
       A.sort()
       for i in range(n):
           s = X-A[i]
           j = i+1
           k = n-1
           while j < k:
               if A[j] + A[k] == s:
                   return 1
               elif A[j] + A[k] < s:
                   j += 1
               else:
                   k -= 1
       return 0



