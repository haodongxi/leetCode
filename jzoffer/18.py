class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return TreeNode类
#
class Solution:
    def Mirror(self,pRoot):
        if pRoot == None:
            return None
        leftNode = pRoot.left
        rightNode = pRoot.right

        pRoot.left = rightNode
        pRoot.right = leftNode

        self.Mirror(leftNode)
        self.Mirror(rightNode)

        return pRoot

if __name__ == "__main__":

    p2 = TreeNode(8)
    p2.left = TreeNode(9)
    p2.left.left = TreeNode(2)

    s = Solution()
    p =  s.Mirror(p2)

    print(p)