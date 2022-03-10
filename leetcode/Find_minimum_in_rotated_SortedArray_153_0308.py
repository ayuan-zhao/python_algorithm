#binary search
#如果middle在右边排序里，我们想搜索左边，如果middle 在左边的排序里，我们想搜索右边
class Solution:
    def findMin(self, nums) -> int:
        left,right = 0,len(nums)-1
        
        while left < right:
            #pivot对数组进行二分,向下取整
            pivot = left + (right - left) //2
            
            #只要是小于右边，右边就会越来越大
            if nums[pivot] <  nums[right]:
                #pivot < right ,min is in left side, update right to the min
                right = pivot
            else:
                #pivot >right, left is sorted,min is in right side
                left = pivot + 1
                #注意细节！返回具体的数而不是坐标
        return nums[left]           
        