class Soluyion:
    def threeSum(self,nums):
    #nums.sort(),从小到大
    #result = []返回 solution set 
    #[-4,-1,-1,0,1,2]combine solution,so we need a loop while/for
    #一上来先判断 最小的三个数相加是不是为零
    #[0,1,2,3,4,5...] 0+1+2 >0
    #[-100,0,1,2,3,4...8,9]
    #-100 + 8 + 9 = -83 < 0,如果最小的数和最大的两个数相加<0，就continue
        n = len(nums)
        result =[]
        nums.sort()

        for i in range(n-2):
            if nums[i] +nums[i+1]+nums[i+2] > 0:
                break
            # get rid of the first lowest number 
            if nums[i] +nums[n-2]+nums[n-1] <0:
                continue
            if 0 < i and nums[i] ==nums[i-1]:
                continue
            left,right = i+1,n-1
            while left < right:
                tmp = nums[i] +nums[left] +nums[right]
                if tmp == 0:
                    #注意append 多个argument时要加括号[]
                    result.append([nums[i],nums[left],nums[right]])
                    while left +1 < right and nums[left] == nums[left +1]:
                        left += 1
                    left += 1     
                    while left < right -1 and nums[right] ==  nums[right-1]
                        right -= 1 
                    right -= 1
                elif tmp < 0:
                    left += 1
                else:
                    right -= 1    
        return result            


