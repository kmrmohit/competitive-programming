'''
Day 3
2 attempts
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, currPath, targetSum):
        result = []
        if root is None:
            return result
        targetSum -= root.val
        currPath.append(root.val)
        if targetSum == 0 and root.left is None and root.right is None:
            result.append(currPath)
        if root.left:
            leftResult = self.dfs(root.left, [*currPath], targetSum)
            result.extend(leftResult) if len(leftResult) > 0 else None
        if root.right:
            rightResult = self.dfs(root.right, [*currPath], targetSum)
            result.extend(rightResult) if len(rightResult) > 0 else None
        return result
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        return self.dfs(root, [], targetSum)