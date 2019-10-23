def smallestDifference(arrayOne,arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    minDiff = float("inf")
    currentDiff = float("inf")
    indexOne = 0
    indexTwo = 0
    results = []
    while indexOne < len(arrayOne) and indexTwo <len(arrayTwo):
        firsNumber = arrayOne[indexOne]
        secondNumber =  arrayTwo[indexTwo]

        if firsNumber < secondNumber:
            currentDiff = secondNumber-firsNumber
            indexOne +=1
        elif firsNumber > secondNumber:
            currentDiff = firsNumber-secondNumber
            indexTwo +=1
        else:
            return [firsNumber,secondNumber]
        if minDiff > currentDiff:
            minDiff = currentDiff
            results =[firsNumber,secondNumber]
    return results