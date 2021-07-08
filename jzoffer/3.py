# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     a = []
#     def printListFromTailToHead(self, listNode):
#         if listNode == None:
#             self.a.reverse()
#             return self.a
#         self.a.append(listNode.val)    
#         return self.printListFromTailToHead(listNode.next)
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        a = []
        while(listNode!=None):
            a.append(listNode.val)
            listNode = listNode.next
        a.reverse()
        return a


if __name__ == '__main__':
    s = Solution()
    listNode1 = ListNode(1)
    listNode2 = ListNode(2)
    listNode3 = ListNode(3)
    listNode1.next = listNode2
    listNode2.next = listNode3
     
    print(s.printListFromTailToHead(listNode1))