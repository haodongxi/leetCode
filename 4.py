from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p = nums1
        q = nums2
        if len(nums1)<len(nums2):
            p = nums2
            q = nums1
        for qnum in q:
            centerNum =  len(p)//2
            if len(p)%2 == 0:
                pass
            else:
                center = p[centerNum]


        