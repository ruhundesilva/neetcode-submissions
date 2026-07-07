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
        levelNodes = []
        nextLevelNodes = []
        levelNodes.append(root)
        while levelNodes:
            curr = []
            for node in levelNodes:
                curr.append(node.val)
                if node.left:
                    nextLevelNodes.append(node.left)
                if node.right:
                    nextLevelNodes.append(node.right)
            res.append(curr)
            levelNodes = nextLevelNodes
            nextLevelNodes = []
        return res
