# -*- coding: utf-8 -*-
import numpy
from numpy import matrix

class Solution:
   def minSubArrayLen(self,nums,totaltarget):
    res = float("inf")
    total = 0
    left = 0
    for right in  range(len(nums)):
        total += nums[right]
        while total >= totaltarget:
            res = min(res,right - left + 1 )
            total = total - nums[left]
            left += 1
    return 0 if res == float("inf") else res       


 




so = Solution()
nums1 = [1, 2, 4, 5, 2, 1]
answer = so.minSubArrayLen(nums1, 13 )
print(answer)

