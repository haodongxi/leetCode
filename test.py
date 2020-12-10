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
s = "([{}])"
s = s.replace("()","")
s = s.replace("{}","")
s = s.replace("[]","")
print(s)

b = [0,1,2]
a = b
b = [9]
print(a)