# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums, target):
        prevmap = {}
        for i,n in enumerate(nums):
            if target - n not in prevmap:
                prevmap[n] = i
            else:
                return[prevmap[target-n],i]    

so = Solution()
nums = [1, 3, 4, 5, 6, 10, 7]
ts = so.twoSum(nums, 15)
print(ts)

