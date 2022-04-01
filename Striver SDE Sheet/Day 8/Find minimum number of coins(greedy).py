#Question Link: https://takeuforward.org/data-structure/find-minimum-number-of-coins/
#Solution Link (Python3): please refer the below complete solution.



denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    coins = 0
    n = 9
    for i in range(n-1,-1,-1):
        while (amount >= denominations[i]):
            amount -= denominations[i]
            coins+=1
            

    return coins


change = int(input())
print(findMinimumCoins(change))
