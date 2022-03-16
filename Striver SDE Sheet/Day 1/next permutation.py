#Question Link: https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=a17b6ce49d681819d684c07e7f8cb168&pid=705146&user=tiabhi1999


class Solution:
    def nextPermutation(self, N, arr):
        pivot = 0
        for i in range(N-1, 0, -1):
            if arr[i-1] < arr[i]:
                pivot = i
                break
            
        if pivot == 0:
            arr.sort()
            return arr
            
        swap = N - 1
        while arr[pivot-1] >= arr[swap]:
            swap -= 1
        
        arr[pivot-1], arr[swap] = arr[swap], arr[pivot-1]
        
        arr[pivot:] = reversed(arr[pivot:])
        
        return arr
        




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
