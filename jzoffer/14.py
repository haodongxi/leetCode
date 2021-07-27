# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @param k int整型 
# @return ListNode类
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindKthToTail(self , pHead , k ):
        if pHead == None:
            return None
        oneHead = pHead
        twoHead = pHead
        i = 0
        while(i<k and twoHead!=None):
            twoHead = twoHead.next
            i += 1
        if i!=k:
            return None
        
        while(twoHead != None):
            oneHead = oneHead.next
            twoHead = twoHead.next
        return oneHead


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
if __name__ == '__main__':
    s = Solution()
    printLink(s.FindKthToTail(constructLinkNode([1,2,3,4,5]),1))