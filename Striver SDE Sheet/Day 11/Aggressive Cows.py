#Question Link: https://takeuforward.org/data-structure/aggressive-cows-detailed-solution/
#Solution (Python3): Refer the below function




def aggressiveCows(stalls, k):
	def ispossible(a, n, cows, minDist):
		count = 1
		lastPlacedCow = a[0]
		for i in range(1,n):
			if (a[i] - lastPlacedCow >= minDist):
				count += 1
				lastPlacedCow = a[i]
		if count >= cows:
			return True
        
		return False
	
	n = len(stalls)
	stalls.sort()
	low = 1
	high = stalls[n - 1] - stalls[0]
	
	while(low <= high):
		mid = (low+high) //2
		if(ispossible(stalls, n, k, mid)):
			low = mid + 1
		else:
			high = mid - 1
	return high
	pass
