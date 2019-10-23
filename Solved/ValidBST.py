def validBST(tree):
    return validBSTHelper(tree, float("-inf"), float("inf"))


def validBSTHelper(tree, minVal, maxVal):
    if tree is None:
        return True
    if tree.value < minVal or tree.value >= maxVal:
        return False
    left = validBSTHelper(tree.left, minVal, tree.value)
    right = validBSTHelper(tree.right, tree.value, maxVal)
    return left and right

