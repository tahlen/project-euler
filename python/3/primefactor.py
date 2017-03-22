# Returns last elem in prime factor list
# Last factor found is always largest factor
def findLargestPrimeFactor(x):
        return primeFactors(x)[-1]

# Finds all prime factors, adds to factorList, returns factorList
def primeFactors(x):        
        primeList = [1, 2]
        factorList = []
        
        if isPrime(x):
                print("Input is prime number")
                return
        
        # Divide num
        while not x == 1:
                if x % primeList[-1] == 0:
                        x = x / primeList[-1]
                        print("appending " + str(primeList[-1]) + " to factorList")
                        factorList.append(primeList[-1])
                else:
                        findNextPrime(primeList)
                        print("appending " + str(primeList[-1]) + " to primeList")
                
        print("Prime factors: " + str(factorList))
        return factorList
                
# Find next prime after primeList[-1] then append to list
def findNextPrime(primeList):

	# Number to test if prime
	# Start at last found prime + 1
	testPrimeNumber =  primeList[-1] + 1

	# Loops until next prime number is found
	while not isPrime(testPrimeNumber):
		testPrimeNumber = testPrimeNumber + 1

        primeList.append(testPrimeNumber)

	return

# Loops until a factor is found or testFactorNumber^2 is larger than testPrimeNumber
# Return False if x < 2
# Return False if factor is found, else True
def isPrime(x):

        if x < 2:
                return False
        
	testPrimeNumber = x
	testFactorNumber = 2

	while testFactorNumber**2 <= testPrimeNumber:
                if testPrimeNumber%testFactorNumber == 0:
                        #print("found factor: " + str(testFactorNumber))
			return False
                testFactorNumber += 1

	return True

while True:
        print("Largest prime factor: " + str(findLargestPrimeFactor(input())))
