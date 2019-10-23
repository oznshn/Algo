def twoNumberSum(arrayInput,targetSum):
     nums = {}
     for i in range(len(arrayInput)):
        currentSum = targetSum - arrayInput[i]
        if currentSum in nums:
            return sorted([currentSum,arrayInput[i]])
        else:
            nums[arrayInput[i]] = True
        return True
