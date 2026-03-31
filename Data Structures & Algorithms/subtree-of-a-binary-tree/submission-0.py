# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        queue = deque([root])
        while queue:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True

        return False

    


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [(p,q)]

        while queue:
            a, b = queue.pop()
            if not a and not b:
                continue
            
            if not a or not b or a.val != b.val:
                return False

            queue.append((a.left, b.left))
            queue.append((a.right, b.right))
        
        return True