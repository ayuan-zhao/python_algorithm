# -*- coding: utf-8 -*-
# 给定一个正整数 n，生成一个包含 1 到 $n^2$ 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# https://leetcode.com/problems/spiral-matrix-ii/
# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.md
# 示例:
# 输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
# 而求解本题依然是要坚持循环不变量原则。

# 模拟顺时针画矩阵的过程:

# 填充上行从左到右
# 填充右列从上到下
# 填充下行从右到左
# 填充左列从下到上
# 这里一圈下来，我们要画每四条边，这四条边怎么画，每画一条边都要坚持一致的左闭右开，或者左开又闭的原则，这样这一圈才能按照统一的规则画下来。

# 那么我按照左闭右开的原则，来画一圈，大家看一下：

from numpy import matrix


class Solution:
    def generateMatrix(self, n: int):
        #-> List[List[int]]
        # 初始化要填充的正方形，先不知道要填什么先用0填充
        # _下划线表示不重要，值不重要，重要的是n循环几次。what's matter is the times the range shows… not its value.
        matrix = [[0] * n for _ in range(n)]
        #  matrix = numpy.empty ((5,5))如果
        left, right  = 0, n - 1
        up, down = 0, n - 1
        # 要填充的数字，从1开始
        number = 1  
        # 从上到下，从左到右不要越界
         # 等于的时候是在同一个位置，也可以停止了，不要重复赋值
        while left < right and up < down:
            # 从左到右填充上边
             # !!!千万写上range,否则只会循环开头和结尾，里面都是0
            for x in range(left, right):
                 # 横着写的时候，row不变，matrix的第一个位置是常量colum[up]
                matrix[up][x] = number
                number += 1

            # 从上到下填充右边
            for y in range(up, down):
                #竖着写的时候，row会变，colum不变，y作为会变的row放在matrix的第一个位置
                matrix[y][right] = number
                number += 1

            # 从右到左填充下边，从后往前输出的时候，一定要加-1！！
            for x in range(right, left, -1):
                #最下边的是down
                matrix[down][x] = number
                number += 1

            # 从下到上填充左边
            for y in range(down, up, -1):
                matrix[y][left] = number
                number += 1

            # !统一缩减范围！不要瞎写，因为中间还会用到这些变量缩小要填充的范围
            left += 1
            right -= 1
            up += 1
            down -= 1

        # 如果阶数为奇数，额外填充一次中
        if n % 2:
            matrix[n // 2][n // 2] = number

        return matrix

    def generateMatrix2(self, n: int):
        matrix = [[0]*n for _ in range(n)]
        rowBegin, rowEnd = 0, n - 1
        colBegin, colEnd = 0, n - 1
        number = 1
        while rowBegin < rowEnd and colBegin < colEnd:
            for x in range(colBegin, colEnd):
                matrix[rowBegin][x] = number
                number += 1

            for y in range(rowBegin, rowEnd):
                matrix[y][colEnd] = number
                number += 1
            for x in range(colEnd, colBegin, -1):
                matrix[rowEnd][x] = number
                number += 1
            for y in range(rowEnd, rowBegin, -1):
                matrix[y][colBegin] = number
                number += 1

            rowBegin += 1
            colEnd -= 1
            rowEnd -= 1
            colBegin += 1
        # if n % 2 !=0:和 if n 
        if n % 2 != 0:
            matrix[n // 2][n // 2] = number
        return matrix


                


so = Solution()
#matrixanswer =so.generateMatrix(5 )  
matrixanswer2 =so.generateMatrix2(5 ) 
#print(matrixanswer)     
print(matrixanswer2)    