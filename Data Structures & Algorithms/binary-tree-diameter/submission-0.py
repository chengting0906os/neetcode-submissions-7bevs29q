# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            cur_node = stack[-1]

            if cur_node.left and cur_node.left not in mp:
                stack.append(cur_node.left)
            
            elif cur_node.right and cur_node.right not in mp:
                stack.append(cur_node.right)
            
            else:
                node = stack.pop()

                l_h, l_d = mp[node.left]
                r_h, r_d = mp[node.right]

                mp[node] = (1 + max(l_h, r_h), max(l_h + r_h, l_d + r_d))
            
        return mp[root][1]
        
       