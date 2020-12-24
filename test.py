a = ['w','d','dsdasdasd','ccc']
b = ['d','w','ccc','dsdasdasd']
print(a==b)
a.sort()
b.sort()
print(a==b)
# str1 = "01234567"
# print(str1[0:0+4])


# a = [0,1,1,1,2,3,4,5]
# for i in range(0,len(a)):
#     if i == 1:
#         del a[i]
# print(a)


# def productNode(l):
#     if len(l)>0:
#         alist = l
#         head = ListNode(alist[0])
#         first = head
#         for a in alist[1:]:
#             head.next = ListNode(a)
#             head = head.next
#         return first
#     else:
#         return None
# def nodeToList(n:ListNode):
#     a = []
#     l = n
#     while l!=None:
#         a.append(l.val)
#         l = l.next
#     return a

# a = [0,1,2,'a']
# b = list(a)
# del a[3]
# print(a)
# print(id(b))
# dict = {"()()":"","2":""}
# dict["()()()"]=1
# print(list(dict.keys()))

# def insertStr(s,target,index):
#     str_list = list(s)
#     str_list.insert(index, target)
#     a_b = ''.join(str_list)
#     return a_b

# print(insertStr("hds","(",2))
# nums = [2,0,0]
# d = {}
# r = 1
# print ( True if len(nums)-1==r else (True if nums[r]!=nums[r+1] else False))
# print(str("1"))
# a = "1,2,3"
# print(a.split(","))
# 1
# [-4,-1,1,2]
# a = None
# a = 1

# print(a)
# s = '([{}])'
# print(s[:1]+s[4:])
# print(s[s.find(']'):])
# print(s.find('1'))
# s = "([{}])"
# s = s.replace("()","")
# s = s.replace("{}","")
# s = s.replace("[]","")
# print(s)

# b = [0,1,2]
# a = b
# b = [9]
# print(a)