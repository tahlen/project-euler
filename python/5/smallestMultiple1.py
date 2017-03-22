def smallestMultiple(arg):
    factorList = range(arg + 1)
    factorList.pop(0)
    factorList.pop(0)
    num = 0
    divisible = False
    while not divisible:
        num += arg
        remainder = 0
        print("num = " + str(num))
        for x in factorList:
            remainder += (num % x)
            print(str(x))
            if remainder != 0:
                break
        if remainder == 0:
            divisible = True
        print("remainder = " + str(remainder))

    return num

while True:
    print(smallestMultiple(input()))
