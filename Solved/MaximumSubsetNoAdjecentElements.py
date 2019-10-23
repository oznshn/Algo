# Write a function that takes in an array of positive integers and returns an integer representing 
# the maximum sum of non-adjacent elements in the array.
#  If a sum cannot be generated,
#  the function should return 0.

#Sample input: [75, 105, 120, 75, 90, 135]
# Output : 330(75,120,135)

# O(n) time | O(n) space

def maxSubSetNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    maxSums = array[:] #copy of array
    maxSums[1]=max(array[0],array[1])
    for i in range(2,len(array)):
        maxSums[i] = max(maxSums[i-1],maxSums[i-2]+array[i])
    return maxSums[-1]

