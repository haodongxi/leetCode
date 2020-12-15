from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        new = lists[0]
        for nodes in lists[1:]:
            new = self.mergeTwoLists(new, nodes)
        return new

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        if p == None and q == None:
            return None
        new = p if p != None else q
        i = 0
        while True:
            if p == None or q == None:
                break
            if p != None and q != None:
                if q.val < p.val:
                    tempQ = q.next
                    q.next = p
                    p = q
                    q = tempQ
                    if i == 0:
                        new = p
                elif q.val >= p.val and p.next == None:
                    p.next = q
                    if i == 0:
                        new = p
                    break
                elif q.val >= p.val and q.val <= p.next.val:
                    tempQ = q.next
                    q.next = p.next
                    p.next = q
                    q = tempQ
                    if i == 0:
                        new = p
                elif p.next.val < q.val:
                    if i == 0:
                        new = p
                    p = p.next

            i = i+1
        return new

    def mergeKLists2(self, lists: List[ListNode]):
        if len(lists) == 0:
            return None
        resultList = []
        while len(lists) > 0:
            minNode = None
            minNum = None
            minIndex = None
            tempList = list(lists)
            for i in range(0, len(tempList)):
                tempNode = tempList[i]
                if tempNode!=None and(minNode == None or minNum > tempNode.val):
                    minNum = tempNode.val
                    minNode = tempNode
                    minIndex = i
            if minNum != None:        
                resultList.append(minNum)
                if minNode.next == None and minIndex!=None:
                    del lists[minIndex]
                elif minIndex!=None:
                    lists[minIndex] = minNode.next
            else:
                break
        return productNode(resultList)


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

if __name__ == "__main__":
    alist = [1, 4, 5]
    blist = [1, 3, 4]
    clist = [2, 6]
    s = Solution()
    # l = s.mergeKLists2([None])
    l = s.mergeKLists2(
        [productNode(alist), productNode(blist), productNode(clist)])
    print(l)
