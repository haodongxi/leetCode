from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        j = n-1
        twoHead = head
        temphead = head
        lastNode = None
        while j > 0:
            twoHead = twoHead.next
            j = j-1
        while True and twoHead!=None:
            if twoHead.next == None:
                if lastNode == None:
                    if head.next!=None:
                        head = head.next
                        break
                    else:
                        return None
                lastNode.next = temphead.next
                break
            else:
                twoHead = twoHead.next
                lastNode = temphead
                temphead = temphead.next
        return head
if __name__ == "__main__":
    s = Solution()
    alist = [1]
    head = ListNode(1)
    first = head
    for a in alist[1:]:
        head.next = ListNode(a)
        head = head.next
    print(s.removeNthFromEnd(first,0))
