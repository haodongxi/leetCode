# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    treeNode = None

    def reConstructBinaryTree(self, pre, tin):
        self.buildTree(pre, tin)
        return self.treeNode

    def buildTree(self, pre, tin):
        if len(pre) > 0:
            centerIndex = tin.index((pre[0]))
            if centerIndex != -1:
                newPre = pre[1:]
                leftTin = tin[0:centerIndex]
                rightTin = tin[centerIndex+1:]
                lefpre = newPre[0:len(leftTin)]
                rightPre = newPre[len(leftTin):]
                treeNode = TreeNode(pre[0])
                if self.treeNode == None:
                    self.treeNode = treeNode
                if len(lefpre) > 0 and len(leftTin) > 0:
                    treeNode.left = self.buildTree(lefpre, leftTin)
                else:
                    treeNode.left = None
                if len(rightPre) > 0 and len(rightTin) > 0:
                    treeNode.right = self.buildTree(
                        rightPre, rightTin)
                else:
                    treeNode.right = None
                return treeNode
            else:
                return None
        else:
            return None


if __name__ == '__main__':
    s = Solution()
    print(s.reConstructBinaryTree(
        [1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7]))
