
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head    
        newHead = None
        lastNode = None
        p = head
        while True:
            tempNodeList = []
            for i in range(0,k):
                if p!=None:
                    tempNodeList.append(p)
                    p = p.next
                else :
                    if i==0:
                        return newHead
                    else:
                        break
            if len(tempNodeList)<k:
                lastNode.next = tempNodeList[0] if len(tempNodeList)>0 else None
                break
            else:
                tempNodeList = tempNodeList[::-1]
                tempSubNode = tempNodeList[0]
                for i in range(1,k):
                    tempSubNode.next = tempNodeList[i]
                    tempSubNode = tempSubNode.next
                tempSubNode.next = None
                if lastNode!=None:
                    lastNode.next = tempNodeList[0]
                else:
                    newHead = tempNodeList[0]
                lastNode = tempNodeList[k-1]
        return newHead

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

    print(nodeToList(s.reverseKGroup(productNode([1,2,3,4,5]),1)))