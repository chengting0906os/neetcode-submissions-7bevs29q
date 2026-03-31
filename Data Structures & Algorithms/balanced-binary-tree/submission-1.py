# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, 0)]
        depth = {}

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            
            if visited:
                left = depth.get(node.left, 0)
                right = depth.get(node.right, 0)

                if abs(left - right) > 1:
                    return False

                depth[node] = 1 + max(left, right)

            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))

        return True