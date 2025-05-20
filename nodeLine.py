from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(node, path:List):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                result.append(path.copy())
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return result
    def binary_tree_paths(self,root):
        if not root:
            return []
        stack = [(root, str(root.val))]
        paths = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
        return paths


if __name__ == '__main__':
    s = Solution()
    # tree1 = TreeNode(1)
    # tree2 = TreeNode(2)
    # tree3 = TreeNode(3)
    # tree1.right = tree2
    # tree2.left = tree3
    tree3 = TreeNode(3)
    tree9 = TreeNode(9)
    tree20 = TreeNode(20)
    tree15 = TreeNode(15)
    tree7 = TreeNode(7)
    tree3.left = tree9
    tree3.right = tree20
    tree20.left = tree15
    tree20.right = tree7
    res = s.binaryTreePaths(tree3)
    print(res)