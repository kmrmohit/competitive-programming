'''
Day 3
1 attempt
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        l,r=0,0
        if node.left:
            l = l + self.dfs(node.left)
        if node.right:
            r = r + self.dfs(node.right)
        return 1+max(l,r)
    def maxDepth(self, root: TreeNode | None) -> int:
        return self.dfs(root)
        