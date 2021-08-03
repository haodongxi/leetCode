# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val == pRoot2.val:
            result = self.handleTree(pRoot1,pRoot2)
            if result == True:
               return True
            else:
                return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
        else:
            return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
            

    def handleTree(self,pRoot1,pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val == pRoot2.val and pRoot2.left == None and pRoot2.right == None:
            return True
        if pRoot1.val == pRoot2.val:
            return self.handleTree(pRoot1.left,pRoot2.left) and self.handleTree(pRoot1.right,pRoot2.right)
        return False
if __name__ == '__main__':
    # p1 = TreeNode(8)
    # p1.left = TreeNode(8)
    # p1.left.left = TreeNode(9)
    # p1.left.left.left = TreeNode(2)
    # p1.left.left.left.left = TreeNode(5)

    # p2 = TreeNode(8)
    # p2.left = TreeNode(9)
    # p2.left.left = TreeNode(2)

    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    p1.left.left = TreeNode(4)
    p1.left.right = TreeNode(5)
    p1.left.right.left = TreeNode(6)

    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    p2.left.left = TreeNode(4)
    p2.left.right = TreeNode(5)


# {1,2,3,4,5,#,#,#,#,6},{1,2,#,4,5}
    s = Solution()
    print(s.HasSubtree(p1,p2))