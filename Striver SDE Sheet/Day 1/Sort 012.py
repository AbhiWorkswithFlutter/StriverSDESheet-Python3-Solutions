#Question link: https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/

#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=767534c5888773d9b35e13af7a0c16fd&pid=702382&user=tiabhi1999


class Solution:
    def sort012(self,arr,n):
        low = 0
        mid = 0
        high = n-1
        
        while(mid<=high):
            if arr[mid] == 0:
                arr[mid],arr[low] = arr[low], arr[mid]
                mid+=1
                low+=1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid],arr[high] = arr[high], arr[mid]
                high -=1
        




if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

