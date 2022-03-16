#Question Link: https://takeuforward.org/data-structure/merge-overlapping-sub-intervals/
#Solution Link (Python3): https://practice.geeksforgeeks.org/viewSol.php?subId=b13dec3d23c5b1f6ba98e48dbca420a9&pid=708874&user=tiabhi1999


class Solution():
    def overlappedInterval(self, Intervals):
        if Intervals == []:
            return []
        result = []
        Intervals.sort()
        for interval in Intervals:
            if result == [] or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1],interval[1])
        return result
      
 
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().strip().split()))
        Intervals = []
        j = 0
        for i in range(n):
            x = a[j]
            j += 1
            y = a[j]
            j += 1
            Intervals.append([x,y])
        obj = Solution()
        ans = obj.overlappedInterval(Intervals)
        for i in ans:
            for j in i:
                print(j, end = " ")
        print()
