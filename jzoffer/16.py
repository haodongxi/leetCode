# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def constructLinkNode(nums):
    subNums = nums[1:]
    firstNode = ListNode(nums[0])
    head = firstNode
    for i,a in enumerate(subNums):
        tempNode = ListNode(a)
        firstNode.next = tempNode
        firstNode = tempNode
    return head
def printLink(head):
    while(head!=None):
        print(head.val)
        head = head.next
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        pHead3 = None
        result = None
        while(pHead1!=None and pHead2!=None):
            Node = None
            if pHead1.val <= pHead2.val:
                Node = pHead1
                pHead1 = pHead1.next
                Node.next = None
            else:
                Node = pHead2
                pHead2 = pHead2.next
                Node.next = None
            if pHead3 == None:
                pHead3 = Node
                result = pHead3
            else:
                pHead3.next = Node
                pHead3 = Node
        if pHead1!=None:
            if pHead3 == None:
                result = pHead1
            else:
                pHead3.next = pHead1
        elif pHead2!=None:
            if pHead3 == None:
                result = pHead2
            else:
                pHead3.next = pHead2
        return result

if __name__ == '__main__':
    s = Solution()
    printLink(s.Merge(None,constructLinkNode([2,4,6])))