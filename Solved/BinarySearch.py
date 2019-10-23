def binarySearch(array,target):
    return binarySearchHelper(array,target,low=0,high=len(array)-1)

def binarySearchHelper(array,target,low,high):
    if low >high:
        return -1
    middle = (low + high)/2
    if array[middle] == target:
        return middle
    elif array[middle]>target:
        return binarySearchHelper(array,target,low,middle-1)
    else:
        return binarySearchHelper(array,target,middle+1,high)
    
