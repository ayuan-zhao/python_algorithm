# -*- coding: utf-8 -*-
class Solution:
    def MaximumSumbarray(self,nums):
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(curSum,maxSub)
        return maxSub  

so = Solution()
an0 = so.MaximumSumbarray([4,6,3,2,-4,6,7,-10,2,3])
an1 = so.MaximumSumbarray([-7,-3,-1,-5,-6])
an2 = so.MaximumSumbarray([-1,-2,-1,-1])
an3 = so.MaximumSumbarray([-1,-2,0,-3,-4])
an4 = so.MaximumSumbarray([1,2,-3,-5,-3,8,-7,6]) 

print("[4,6,3,2,-4,6,7,-10,2,3]")
print(an0) 
print("([-7,-3,-1,-5,-6])")
print(an1) 
print("[-1,-2,-1,-1])")
print(an2) 
print("[-1,-2,0,-3,-4])")
print(an3) 
print("[1,2,-3,-5,-3,8,-7,6]")
print(an4) 


        

    
