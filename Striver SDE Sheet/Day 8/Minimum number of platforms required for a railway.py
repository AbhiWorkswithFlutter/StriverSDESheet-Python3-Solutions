#Question Link: https://takeuforward.org/data-structure/minimum-number-of-platforms-required-for-a-railway/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=f446a71d75caebcbde628afe7bca7ded&pid=701368&user=tiabhi1999

class Solution:
    
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        
        i = 1
        j = 0
        plat = 1
        result = 1
        while(i<n and j < n):
            if arr[i] <= dep[j]:
                plat += 1
                i+=1
            elif arr[i] > dep[j]:
                plat -= 1
                j+=1
            if plat > result:
                result = plat
        return result

   


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
