# Definition for singly-linked list.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        i = 0
        res = lists[0]
        while len(lists[i+1:]) > 0:
            node = lists[i+1]
            while node != None:
                res = self.sortNode(res,node)
                node = node.next
            i += 1

        return res

    def sortNode(self,res:ListNode,node:ListNode):
        if res == None:
            return node
        if node == None:
            return res
        a = res 
        record = None
        while True:
            if a == None:
                record.next = node
                return res
            if a.next == None:
                a.next = node
                return res
            if a.val <= node.val:
                record = a
                a = a.next
            else:
                if record == None:
                    node.next = res
                    return node
                else:  
                    record.next = node
                    node.next = a
                    return res      



def generateNodeList(int_list:List[List[int]]) -> List[ListNode]:
    
    res = []
    for i in range(0,len(int_list)):
        pass
    return res 


if __name__ == '__main__':
    pass