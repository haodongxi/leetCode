# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root == None:
            return []
        pool = []
        pool.append(root)
        result = []
        while(len(pool)>0):
            tempNode = pool[0]
            del pool[0]
            result.append(tempNode.val)
            if tempNode.left!=None:
                pool.append(tempNode.left)
            if tempNode.right!=None:
                pool.append(tempNode.right)
        return result