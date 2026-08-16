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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered = self.inord(root)
        return ordered[k - 1]