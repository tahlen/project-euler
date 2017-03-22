def smallestMultiple(arg):
    factorList = range(arg + 1)
    factorList.pop(0)
    factorList.pop(0)

    #for factor in factorList:
    #    if (factor != 2) and (factor % 2 == 0):
    #        factorList.remove(factor)
    
    x = 1
    for factor in factorList:
        x *= factor
    
    multipleList = range(x+1)
    multipleList.pop(0)
    multipleList.pop(0)
    multipleList.pop(0)
        
    for factor in factorList:
        multipleList = filterList(factor, multipleList)
        print('Factor: ' + str(factor))
        print('list: ' + str(multipleList))

    return multipleList[0]

def filterList(x, argList):
    numList = []
    for item in argList:
        if (item % x) == 0:
            numList.append(item)

    return numList
    
while True:
    print(smallestMultiple(input()))
