# -*- coding: utf-8 -*-
import numpy
from numpy import matrix

class Solution:
    def search(self,nums,target):
        left,right = 0,len(nums)-1
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle- 1
            else :
                return middle
        return -1               
         
so = Solution()
nums1= [1,2,4,5,6,7,8]
res = so.search(nums1,2)
print(res)


