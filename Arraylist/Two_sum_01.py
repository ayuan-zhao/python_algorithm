# -*- coding: utf-8 -*-

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 字符串、整数等都是不可变的，因此，可以放心地作为key，而list是可变的，就不能作为key：


class Solution:
    # 暴力解
    def twoSumBaoLi0(self, nums, target):
        for i in nums:
            # 因为两数相加等于target,所以先循环一个，另一个是target - i
            j = target - i
            # 取这个数组的index nums.index(i)
            start_index = nums.index(i)
            next_index = start_index + 1
            # 重新建了一个array,nums[next_index:]打到最后
            temp_nums = nums[next_index:]
            if j in temp_nums:
                # 如果就是下一个，就是next_index + temp_nums.index(j), 只不过这时，temp_nums.index(j) = 0
                return(nums.index(i), next_index + temp_nums.index(j))

    def twoSum1(self, nums, target):
        # 建一个新的dictionary
        dict = {}
        for i in range(len(nums)):
            #一个数是否 in dict,这是在查找key是不是存在
            if target - nums[i] not in dict:
                # nums[i]是key,nums里具体的数是key,indexing是value,每次把扫到的数存到dict里,然后检查，target -目前扫到的数在不在dic里
                # 比如寻找15，就15-2，看看有没有13，没有就dict[2:0],然后15-5，看看有没有10，没有就存dict[2:0,5:1],然后15-10，看看有没有5
                # 发现dict中的key有5，然后就返回
                # 当我们用target- nums[i],得到的那个值在 dic
                dict[nums[i]] = i
            else:
                # dict[target-nums[i]]
                return [dict[target - nums[i]], i]

    def twoSumOpt2(self, nums, target):
        prevmap = {}  # 会设key是nums的value，value是nums的indexing
        # 这里的i是indexing,n是value
        for i, n in enumerate(nums):
            # 找的是这个key
            if target - n in prevmap:
                # prevmap[target - n] 这个整体是prevmap的value是indexing，i 本身就是indexing
                return [prevmap[target - n], i]
            prevmap[n] = i
           # print(prevmap)
        return

    def twoSumfinal3(self, nums, target):
        prevmap = {}
        for i, n in enumerate(nums):
            if target - n not in prevmap:
                prevmap[n] = i
            else:
                return [prevmap[target - n], i]

    def twoSumbasic4(self, nums, target):
        prevmap = {}
        for i in range(len(nums)):
            if target - nums[i] not in prevmap:
                prevmap[nums[i]] = i
            else:
                return [prevmap[target - nums[i]], i]


so = Solution()
nums = [1, 3, 4, 5, 6, 10, 7]
ts0 = so.twoSumBaoLi0(nums, 15)
print(ts0)

so = Solution()
nums = [1, 3, 4, 5, 6, 10, 7]
ts1 = so.twoSum1(nums, 15)
print(ts1)

so = Solution()
nums = [1, 3, 4, 5, 6, 10, 7]
# prevmap 最后的样子{1: 0, 3: 1, 4: 2, 5: 3, 6: 4}
ts2 = so.twoSumOpt2(nums, 15)
print(ts2)

so = Solution()
nums = [1, 3, 4, 5, 6, 10, 7]

ts3 = so.twoSumfinal3(nums, 15)
print(ts3)

so = Solution()
nums = [1, 3, 4, 5, 6, 10, 7]
ts4 = so.twoSumbasic4(nums, 15)
print(ts4)

#返回坐标，最好还是[]方括号吧
# 4 - 1 = 3, we just check if 3 is exist
# use hash map
# maping the value to the index
# 为什么要建一个新的hash map而不是直接把list放入hash map,直接去查
# 因为，每个元素不能用两遍，比如target是4， 4-2 = 2,2已经在里面了

# print ( "i=", i, "n=" , n, "target", target, "target - n= ", target - n)
#                 print("prevmap[target - n]", prevmap[target - n])
# it can be initially empty
# iterate through the array   O（N）
# adding each value to our hash map————constant time
# checking if a value exists in our hash ——————constant time
