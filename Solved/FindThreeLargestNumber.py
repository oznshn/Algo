def findThreeLargestNumber(array):
    largest= [None,None,None]
    for num in array:
        updateLargetsNumber(largest,num)
    return largest

def updateLargetsNumber(largest,num):
    if largest[2] is None or num >largest[2]:
        largest[0]=largest[1]
        largest[1]=largest[2]
        largest[2] = num 
    elif largest[1] is None or num > largest[1]:
        largest[0]=largest[1]
        largest[1] = num
    elif largest[0] is None or num > largest[0]:
        largest[0] = num

input= [141,17,-2,-7,-17,-27,18,541,8,7,7]

findThreeLargestNumber(input)