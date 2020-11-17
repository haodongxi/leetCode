class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len1 = 0
        len2 = 0
        p = l1
        q = l2
        while p!=None:
            len1 = len1+1
            p = p.next
        while q!=None:
            len2 = len2+1
            q = q.next
        if len1>len2:
            p = l1
            q = l2
        else :
            p = l2
            q = l1
        more = 0
        sum = ListNode()
        r = sum
        while p !=None:
            r.val = (p.val+q.val+more)%10
            more =  (p.val+q.val+more)//10
            if p.next!=None:
                r.next = ListNode()
                r = r.next
            p =  p.next
            if q.next != None:
                q = q.next
            else :
                q.next = ListNode()
                q = q.next
        if more>0:
            r.next = ListNode()
            r.next.val = 1
        r = sum
        while r!=None:
            print(r.val)
            r = r.next
        return sum
if __name__ == "__main__":
    l1 = ListNode()
    l2 = ListNode()
    p = l1
    q = l2
    list1 = [9,9,9,9,9,9,9]
    list2 = [9,9,9,9]
    for i in range(0,len(list1)):
        p.val = list1[i]
        if i<len(list1)-1:
            p.next = ListNode()
            p = p.next
    for i in range(0,len(list2)):
        q.val = list2[i]
        if i<len(list2)-1:
            q.next = ListNode()
            q = q.next     
    s = Solution()
    s.addTwoNumbers(l1,l2)