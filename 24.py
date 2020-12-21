from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        l = head
        lastNode = None
        while l!=None:
            if l.next!=None:
                tempNode = l.next
                l.next = l.next.next
                tempNode.next = l
                if lastNode!=None:
                    lastNode.next = tempNode
                else:
                    head = tempNode
                lastNode = l
                l = l.next
            else:
                break
        return head
def productNode(l):
    if len(l)>0:
        alist = l
        head = ListNode(alist[0])
        first = head
        for a in alist[1:]:
            head.next = ListNode(a)
            head = head.next
        return first
    else:
        return None
def nodeToList(n:ListNode):
    a = []
    l = n
    while l!=None:
        a.append(l.val)
        l = l.next
    return a
if __name__ == "__main__":
    s = Solution()
    print(nodeToList(s.swapPairs(productNode([]))))
    