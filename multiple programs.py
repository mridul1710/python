#remember to remove pass once start coding
def is_prime(numToCheck):
	for i in range(2, numToCheck):
		if numToCheck % i == 0:
			return False
	return True

def all_primes(num):
	primes = []
	for i in range(2, num + 1):
		if is_prime(i):
			primes.append(i)
	
	return len(primes)


def pascal_triangle(numRows):
	pt = []
	for i in range(0, numRows):
		currentRow = []
		for j in range(0, i + 1):
			if j == 0 or j == i:
				currentRow.append(1)
			else:
				currentRow.append(pt[i - 1][j - 1] + pt[i - 1][j])
		pt.append(currentRow)

	return pt


def maxProfit(prices):
	#maximum profit
	mp = 0

	for i in range(0, len(prices)):
		buy = prices[i]
		for j in range(i, len(prices)):
			sell = prices[j]
			profit = sell - buy
			if profit > mp:
				mp = profit

	return mp




#Calling functions to test out code; check out what the expected output should be on the assignment description

#should print 4
print(all_primes(7))

#should print 8
print(all_primes(20))

#should print [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(pascal_triangle(5))


#should print [[1]]
print(pascal_triangle(1))


#should print 5
print(maxProfit([7,1,5,3,6,4]))

#should print 0
print(maxProfit([7,6,4,3,1]))