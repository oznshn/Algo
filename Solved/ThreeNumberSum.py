def TreeNumberSum(inputArr,targetSum):
    inputArr.sort()
    results = []
    for i in range(len(inputArr)-2):
        left = i+1
        right = len(inputArr)-1
        while left < right:
            currentSum = inputArr[i]+ inputArr[left]+inputArr[right]
            if currentSum == targetSum:
                results.append([inputArr[i], inputArr[left],inputArr[right]])
            elif currentSum < targetSum:
                left += 1
            elif currentSum >targetSum:
                right -=1
    return results

