#Question Link: https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=1c9194bac1c9e76550d068e87479c2ce&pid=700246&user=tiabhi1999


class Solution:    
    def remove_duplicate(self, arr, N):
        i = 0
        for j in range(1,N):
            if (arr[i] != arr[j]):
                i += 1
                arr[i] = arr[j]
   
        return i + 1
        


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()

