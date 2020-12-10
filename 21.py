class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        if p == None and q == None:
            return None
        new = p if p !=None else q
        i = 0
        while True:
            if p==None or q==None:
                break
            if p!=None and q!=None:
                if q.val<p.val:
                    tempQ = q.next
                    q.next = p
                    p = q
                    q = tempQ
                    if i == 0:
                        new = p
                elif q.val>=p.val and p.next==None:
                    p.next = q
                    if i == 0:
                        new = p
                    break
                elif q.val>=p.val and q.val<=p.next.val:
                    tempQ = q.next
                    q.next = p.next
                    p.next = q
                    q = tempQ
                    if i == 0:
                        new = p
                elif p.next.val<q.val:
                    if i == 0:
                        new = p
                    p = p.next

            i = i+1
        return new

    def listNodelength(self,l:ListNode):
        n = 0
        while l!=None:
            n = n+1
            l = l.next
        return n

if __name__ == "__main__":

    alist = [-9,3]
    head = ListNode(-9)
    first = head
    for a in alist[1:]:
        head.next = ListNode(a)
        head = head.next

    blist = [5,7]
    tHead = ListNode(5)
    second = tHead
    for a in blist[1:]:
        tHead.next = ListNode(a)
        tHead = tHead.next
    s= Solution()
    l = s.mergeTwoLists(first,second)
    print(l)
    