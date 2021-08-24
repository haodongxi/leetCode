
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# @param pRootOfTree TreeNode类 
# @return TreeNode类
#
class Solution:
    a = []
    def Convert(self , pRootOfTree:TreeNode):
        self.ReadFromCenter(pRootOfTree)
        
        for (index,value) in enumerate(self.a):
            if index+1<len(self.a):
                value.right = self.a[index+1]
            else:
                value.right = None
            if index-1>=0:
                value.left = self.a[index-1]
            else:
                value.left = None
        return self.a[0] if len(self.a)>0 else None
        
    def ReadFromCenter(self,pRootOfTree:TreeNode):
        if pRootOfTree == None:
            return 
        if pRootOfTree.left == None and pRootOfTree.right == None:
            self.a.append(pRootOfTree)
            return
        leftNode = pRootOfTree.left
        rightNode = pRootOfTree.right
        self.ReadFromCenter(leftNode)
        self.a.append(pRootOfTree)
        self.ReadFromCenter(rightNode)
if __name__ == "__main__":
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    p1.left.left = TreeNode(4)
    p1.left.right = TreeNode(5)
    p1.left.right.left = TreeNode(6)


    s = Solution()
    s.Convert(p1)

    
