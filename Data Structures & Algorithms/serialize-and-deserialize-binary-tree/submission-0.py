# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def preord(self, root, res):
        if not root:
            res.append(' ')
            return
        res.append(root.val)
        self.preord(root.left, res)
        self.preord(root.right, res)
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        l = []
        self.preord(root, l)
        b = [str(x) for x in l]
        return ','.join(b)

    def buildTree(self, data, index):
        data_list = data.split(',')
        if data_list[index[0]] == ' ':
            index[0]+=1
            return None
        tree = TreeNode()
        tree.val = data_list[index[0]]
        index[0]+=1
        tree.left = self.buildTree(data, index)
        tree.right = self.buildTree(data, index)
        return tree
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        index = [0]
        return self.buildTree(data, index)
