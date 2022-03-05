class Solution:
    def productExceptSelf(self, nums):
        # 先确定好边界
        length = len(nums)
        # !!!注意不要写left=right=answer=[0]*length，这样等于是三个指针指向同一个内存了。
        left, right, answer = [0]*length, [0]*length, [0]*length
        # right =[0]*length
        # answer = [0]*length
        # 第一个位置上不乘以任何数，所以设为1，乘积是它本身
        left[0] = 1
        for i in range(1, length):
            #每次记录左边的乘积
            left[i] = nums[i-1]*left[i-1]
        right[length - 1] = 1
        for i in reversed(range(length - 1)):
            right[i] = nums[i + 1]*right[i + 1]

        for i in range(length):
            answer[i] = left[i]*right[i]
        return answer


so = Solution()
ans = so.productExceptSelf([1, 2, 6, 2, 4, 5])
print(ans)
