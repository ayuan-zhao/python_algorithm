# -*- coding: utf-8 -*-

class Solution:
    #这个是最好理解的
    def maximumSubarray0(self,nums):
        #max_end的意思是一直打到最后
        max_end = max_so_far = nums[0]
        for item in nums[1:]:
            #是加上前面的大，还是独立的一个最大
            max_end = max(item,max_end + item)
            #只要不是前面加一起都不如单独的一个新数大，那
            max_so_far = max(max_so_far,max_end)
        return max_so_far

    def MaximumSumbarray(self, nums):
        if max(nums) < 0:
            return max(nums)
            #如果都是小于零，那就越加越小
            #这是预设的都为0，如果都预设是数组第一个数，local_max = max(num, local_max + num)
            #就不用先排除负数了
        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max, local_max)
        return global_max

    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            #if prefix前缀 < 0,cut it off,从这一个开始加
            #因为初始值设为是0，因为如果加出负数来，说明加了上一个数就亏了，
            #又因为要连续的subArray,所以只能把前面所有都清零。
            if curSum < 0:
                curSum = 0
            #这步的位置很关键，curSum总是要加当前数后再和maxSub比，这样即使nums都是负数，maxSub也会用存的最小负数和curSum存的当前的负数比，哪个更大，返回大的
            #重新设置prefix
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
        
so = Solution()
an0 = so.maximumSumbarray([4,6,3,2,-4,6,7,-10,2,3])
an1 = so.maximumSumbarray([-7,-3,-1,-5,-6])
an2 = so.maximumSumbarray([-1,-2,-1,-1])
an3 = so.maximumSumbarray([-1,-2,0,-3,-4])
an4 = so.maximumSumbarray([1,2,-3,-5,-3,8,-7,6]) 

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


an0 = MaximumSubarray0([4,6,3,2,-4,6,7,-10,2,3])
an1 = MaximumSubarray0([-7,-3,-1,-5,-6])
an2 = MaximumSubarray0([-1,-2,-1,-1])
an3 = MaximumSubarray0([-1,-2,0,-3,-4])
an4 = MaximumSubarray0([1,2,-3,-5,-3,8,-7,6]) 

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
