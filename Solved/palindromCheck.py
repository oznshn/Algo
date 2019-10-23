def palindromCheck(input):
    newInput=""
    for i in range(len(input)):
        newInput = newInput+input[i]
    return newInput == input