'''
Day 4
1 attempt
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        que = deque()
        result = []
        que.append((root,1))
        currDepth = 1
        currSet = []
        while que:
            (node, depth) = que.popleft()
            if not node:
                continue
            if depth == currDepth:
                currSet.append(node.val)
            else:
                result.append(currSet)
                currSet = [node.val]
                currDepth = depth
            que.append((node.left, depth+1))
            que.append((node.right, depth+1))
        
        if currSet:
            result.append(currSet)

        return result