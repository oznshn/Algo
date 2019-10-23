def findClosestValue(tree,target):
    return findClosestValueHelper(tree,target,closest=float("inf"))

def findClosestValueHelper(tree,target,closest):
    if tree is None:
        return closest
    
    if abs(target-closest)<abs(target-tree.value):
        closest= tree.value
    
    if target < tree.value:
        findClosestValueHelper(tree.left,target,closest)
    elif target > tree.value:
        findClosestValueHelper(tree.right,target,closest)
    else:
        return closest