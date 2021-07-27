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
    # 返回ListNode
    def ReverseList(self, pHead):
        result = []
        self.ReverseList1(pHead,result)
        if len(result) == 1:
            return result[0]
        else:
            return None
    def ReverseList1(self, pHead,result):
        if pHead == None:
            if len(result) == 0:
                result.append(None)
            return None
        if pHead.next == None:
            if len(result) == 0:
                result.append(pHead)
            return pHead
        if pHead.next.next == None:
            pHead.next.next = pHead
            if len(result) == 0:
                result.append(pHead.next)
            pHead.next = None
            return pHead
        tempHead = pHead
        nextHead = self.ReverseList1(pHead.next,result)
        nextHead.next = tempHead
        tempHead.next = None
        return tempHead



if __name__ == "__main__":
    s = Solution()
    printLink(s.ReverseList(constructLinkNode([233213,4343243,54545])))