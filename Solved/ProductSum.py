def productSum(array):
    return productSumHelper(array,level=1)

def productSumHelper(array,level):
    total = 0
    for elem in array:
        if type(elem) is list:
            total += productSumHelper(elem,level+1)
        else:
            total += elem
    return total * level