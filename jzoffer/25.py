# -*- coding:utf-8 -*-
from typing import List, OrderedDict


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead:RandomListNode):
        tempHead = pHead
        link_map = OrderedDict()
        while pHead!=None:
            if pHead.random!=None:
                link_map[id(pHead)] = [pHead.label,id(pHead.random)]
            else:
                link_map[id(pHead)] = [pHead.label,None]
            pHead = pHead.next
        

        if len(link_map)>0:
            i = 0
            while i<len(link_map):
                key = list(link_map.keys())[i]
                node =  RandomListNode(link_map[key][0])
                link_map[key].append(node)
                i+=1
            i = 0
            while i<len(link_map):
                key = list(link_map.keys())[i]
                currentNode = link_map[key][2]
                nextNode =  None if link_map[key][1] == None  else link_map[link_map[key][1]][2]
                if i == len(link_map)-1:
                    currentNode.next = None
                    currentNode.random = nextNode
                else:
                    nextkey = list(link_map.keys())[i+1]
                    currentNode.next = link_map[nextkey][2]
                    currentNode.random = nextNode
                i+=1
            newHead =  link_map[list(link_map.keys())[0]][2]
            return newHead
        else:
            return None



if __name__ == '__main__':
    node1 = RandomListNode(1) 
    node2 = RandomListNode(2)
    node1.next = node2
    node2.next = None
    node2.random = node1
    node1.random = node2
    s = Solution()
    print(s.Clone(node1))