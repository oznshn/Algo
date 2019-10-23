
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


class Solution:

    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum


    def dfs(self, node):
        if not node:
            return 0

        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))
        self.max_sum = max(self.max_sum, left + right + node.value)
        return max(left, right) + node.value


test = BinaryTree(1).insert(
    [-10, 9, 20, None, None, 15,7])
x =  Solution()
x.maxPathSum(test)
