from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        self.bfs_pre(root,res)
        return res
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        self.bfs_middle(root,res)
        return res
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        self.bfs_suffix(root,res)
        return res
    def bfs_pre(self,root:TreeNode,res:List):
        if root != None:
            res.append(root.val)
            if root.left != None:
                self.bfs_pre(root.left,res)
            if root.right != None:
                self.bfs_pre(root.right,res)
    def bfs_middle(self,root:TreeNode,res:List):
        if root != None:
            if root.left != None:
                self.bfs_middle(root.left,res)
            res.append(root.val)
            if root.right != None:
                self.bfs_middle(root.right,res)
    def bfs_suffix(self,root:TreeNode,res:List):
        if root != None:
            if root.left != None:
                self.bfs_suffix(root.left,res)
            if root.right != None:
                self.bfs_suffix(root.right,res)
            res.append(root.val)

if __name__ == '__main__':
    s = Solution()
    # tree3 = TreeNode(3)
    # tree9 = TreeNode(9)
    # tree20 = TreeNode(20)
    # tree15 = TreeNode(15)
    # tree7 = TreeNode(7)
    # tree3.left = tree9
    # tree3.right = tree20
    # tree20.left = tree15
    # tree20.right = tree7
    # res = s.preorderTraversal(tree3)


    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree1.right = tree2
    tree2.left = tree3
    res = s.preorderTraversal(tree1)
    print(res)
