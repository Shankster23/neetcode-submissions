# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inord(self, root):
        if root == None:
            return []
        return self.inord(root.left) + [root.val] + self.inord(root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        L = self.inord(root)
        for i in range(len(L) - 1):
            if(L[i + 1] <= L[i]):
                return False
        return True
