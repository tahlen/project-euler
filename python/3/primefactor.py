#primeList = [1, 2]

def findNextPrime(x):
	foundPrime = False

	# Number to test if prime
	# Start at last found prime + 1
	testPrimeNumber =  x #primeList[-1]

	# Loops until next prime number is found
	while foundPrime == False:
		testPrimeNumber = testPrimeNumber + 1
		foundPrime = isPrime(testPrimeNumber)

	#primeList.append(testPrimeNumber)
	return

# Loops until a factor is found or testFactorNumber^2 is larger than testPrimeNumber
# Return False if factor is found, else True
def isPrime(x):
	testPrimeNumber = x
	testFactorNumber = 1

	while testFactorNumber^2 < testPrimeNumber:
		testFactorNumber += 1
		if testPrimeNumber%testFactorNumber != 0:
			return False

	return True

while True:
	print(findNextPrime(input()))