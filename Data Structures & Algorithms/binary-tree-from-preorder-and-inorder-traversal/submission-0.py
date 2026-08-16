# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            node = TreeNode()
            node.val = preorder[0]
            return node
        hash_map = dict()
        head_root = TreeNode()
        head_root.val = preorder[0]
        for i in range(len(inorder)):
            hash_map[inorder[i]] = i
        root_idx = hash_map[preorder[0]]
        left_size = root_idx
        left = self.buildTree(preorder[1:1 + left_size], inorder[0:root_idx])
        right = self.buildTree(preorder[(1 + left_size):], inorder[(root_idx + 1):len(preorder)])
        head_root.left = left
        head_root.right = right
        return head_root