def findFibNum(maxNumber):
    numberListAll = [1, 2]
    numberListEven = [2]

    while True:
        temp = numberListAll[-1] + numberListAll[-2]
        if temp%2 == 0:
        	numberListEven.append(temp)
        if temp >= maxNumber:
            break
    	numberListAll.append(temp)

    print(numberListAll)
    print(numberListEven)
    return sum(numberListEven)

while True:
    print('sum = ' + str(findFibNum(int(input()))))

