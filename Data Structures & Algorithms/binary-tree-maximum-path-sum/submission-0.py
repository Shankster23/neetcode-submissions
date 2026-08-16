# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float('-inf')]
        def helper(node):
            if node == None:
                return 0
            elif node.left == None and node.right == None:
                max_sum[0] = max(max_sum[0], node.val)  # just the leaf
                return node.val
            elif node.left == None:
                right_best = helper(node.right)
                max_sum[0] = max(max_sum[0], node.val, node.val + max(0, right_best))
                return node.val + max(0, right_best)
            elif node.right == None:
                left_best = helper(node.left)
                max_sum[0] = max(max_sum[0], node.val, node.val + max(0, left_best))
                return node.val + max(0, left_best)
            else:
                lres = helper(node.left)
                rres = helper(node.right)
                through_node = node.val + max(0, lres) + max(0, rres)
                print(node.val, lres, rres, through_node)
                max_sum[0] = max(max_sum[0], node.val, through_node)
                return max(node.val, node.val + max(0, lres), node.val + max(0, rres))
        helper(root)
        return max_sum[0]