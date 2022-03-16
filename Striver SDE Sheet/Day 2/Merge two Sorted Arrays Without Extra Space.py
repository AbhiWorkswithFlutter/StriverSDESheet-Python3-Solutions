#Question Link: https://takeuforward.org/data-structure/merge-two-sorted-arrays-without-extra-space/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=77a783170fed0233e29fc7d88bb4c85f&pid=701243&user=tiabhi1999

#This was a bit controversial question for me, as I prefer solving this with min heap method(But it has greater time complexity),
#but here I have solved it with Gap method (Shell sort), which was explained by Striver.
#Please refer the gfg link for complete code snippet and question (https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1#)
class Solution:
    #Function to find next gap
    def nextGap(self,gap):
        if (gap <= 1):
            return 0
        else:
            return (gap // 2) + (gap % 2)
        
    def merge(self,arr1,arr2,n,m):
        
        gap = n + m
        gap = self.nextGap(gap)
        while gap > 0:
     
            i = 0
            while i + gap < n:
                if (arr1[i] > arr1[i + gap]):
                    arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
     
                i += 1
     
            j = gap - n if gap > n else 0
            while i < n and j < m:
                if (arr1[i] > arr2[j]):
                    arr1[i], arr2[j] = arr2[j], arr1[i]
     
                i += 1
                j += 1
     
            if (j < m):
                j = 0
                while j + gap < m:
                    if (arr2[j] > arr2[j + gap]):
                        arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
     
                    j += 1
     
            gap = self.nextGap(gap)
     
    



if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
