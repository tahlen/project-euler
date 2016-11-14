def sumOfNumbers(arg):
	numbers = []
	for i in range (1, int(arg)):
		if i%3 == 0 or i%5 == 0:
			numbers.append(i)

	total = 0
	for i in numbers:
		total += i

	return total

while True:
        print(sumOfNumbers(input()))
