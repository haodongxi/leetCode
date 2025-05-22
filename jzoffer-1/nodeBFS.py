
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        self.output([root],res)
        return res

    def output(self,node_list:List[Optional[TreeNode]],res:List):
        if len(node_list) == 0:
            return
        temp_val_list = []
        temp_child_list = []
        for node in node_list:
            if node.val != None:
               temp_val_list.append(node.val)   
            if node.left != None:
                temp_child_list.append(node.left)
            if node.right != None:
                temp_child_list.append(node.right)
        res.append(temp_val_list)
        self.output(temp_child_list,res)


if __name__ == '__main__':
    s = Solution()
    tree3 = TreeNode(3)
    tree9 = TreeNode(9)
    tree20 = TreeNode(20)
    tree15 = TreeNode(15)
    tree7 = TreeNode(7)
    tree3.left = tree9
    tree3.right = tree20
    tree20.left = tree15
    tree20.right = tree7
    res = s.levelOrder(tree3)
    print(res)