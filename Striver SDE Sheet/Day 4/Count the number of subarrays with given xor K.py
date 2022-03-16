#Question Link: https://takeuforward.org/data-structure/count-the-number-of-subarrays-with-given-xor-k/
#The solution is mentioned below in Python3 (Solved in Coding Ninjas IDE)


def subarraysXor(arr, x):
    ans = 0
    xor = 0
    d = {}
    
    for i in range(len(arr)):
        xor ^= arr[i]
        
        if xor == x:
            ans += 1
        
        temp = xor ^ x
        
        if temp in d:
            ans += d[temp]
        if xor in d:
            d[xor] += 1
        else:
            d[xor] = 1
    return ans

arr = list(map(int, input().split()))

x = int(input())

print(subarraysXor(arr, x))
