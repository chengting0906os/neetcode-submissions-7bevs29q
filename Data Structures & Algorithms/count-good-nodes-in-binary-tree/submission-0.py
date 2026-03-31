# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        queue = deque([(root, float('-inf'))]) 
        

        while queue:
            node, max_value = queue.popleft()
            if node.val >= max_value:
                res += 1
            max_value = max(max_value, node.val)
            if node.left:
                queue.append((node.left, max_value))
            if node.right:
                queue.append((node.right, max_value))
        
        return res
        