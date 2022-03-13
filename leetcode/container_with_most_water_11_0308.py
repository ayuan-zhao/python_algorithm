class Solution:
    def maxArea(self, height):
        # maximize the area,make the width to be as big as possible
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            # bottleneck短板，瓶颈 = minimum height
            area = min(height[left], height[right])*(right - left)
            if area > result:
                result = area
            # 判断移动哪边的指针，尽量保留最大的值
            if height[left] < height[right]:
                left += 1
            else:
                #注意right是要-= 1
                right -= 1
        return result

    def maxAreaBruteForce(self, height):
        res = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                area = (right - left) * min(height[left], height[right])
                res = max(res, area)

        return res
