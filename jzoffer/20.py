# -*- coding:utf-8 -*-
class Solution:
    list = []
    minList = []
    def push(self, node):
        self.list.append(node)
        if len(self.minList) == 0:
            self.minList.append(node)
        elif node<=self.minList[-1]:
            self.minList.append(node)
    def pop(self):
        if len(self.list)>0 and len(self.minList)>0 and self.list[-1] == self.minList[-1]:
            self.minList.pop()
        self.list.pop()
    def top(self):
        if len(self.list)>0:
            return self.list[-1]
        return None
    def min(self):
        if len(self.minList)>0:
            return self.minList[-1]
        else:
            return None