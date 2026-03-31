# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        queue = deque([root])
        while queue:
            layer_list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    layer_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if layer_list:
                res.append(layer_list)
        
        return res

            