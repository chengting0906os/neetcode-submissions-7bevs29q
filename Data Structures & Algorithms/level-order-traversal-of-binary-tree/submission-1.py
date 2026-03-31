# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            layer_val_list = []
            new_layer = []
            for s in stack:
                layer_val_list.append(s.val)
                if s.left:
                    new_layer.append(s.left)
                if s.right:
                    new_layer.append(s.right)
            
            res.append(layer_val_list)
            stack = new_layer
        
        return res

            