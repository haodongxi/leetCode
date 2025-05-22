
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def printRoad(node):
    if node == None:
        return
    
    def bfs(node,res):
        if not node :
            return
        res.append(node.val)
        if  not node.left and not node.right:
            res_copy = res.copy()
            print(res_copy)
        else:
            bfs(node.left,res)
            bfs(node.right,res)
        res.pop()

    bfs(node,[])
            

def zs_bfs(node):
    if not node:
        return []
    return [node.val] + zs_bfs(node.left) +zs_bfs(node.right)
    

def no_zs_bfs(node):
    stack = [node]
    res = []
    while len(stack) >0:
        s = stack.pop()
        res.append(s.val)
        if s.right != None:
            stack.append(s.right)
        if s.left != None:
            stack.append(s.left)
    return res    

if __name__ == '__main__':
    tree3 = TreeNode(3)
    tree9 = TreeNode(9)
    tree20 = TreeNode(20)
    tree15 = TreeNode(15)
    tree7 = TreeNode(7)
    tree3.left = tree9
    tree3.right = tree20
    tree20.left = tree15
    tree20.right = tree7
    # printRoad(tree3)
    print(no_zs_bfs(tree3))