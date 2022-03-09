# -*- coding: utf-8 -*-
# #Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]] 
# join()将序列中的元素以指定的字符连接生成一个新的字符串。
# #s1 = "-"
# s2 = ""
# seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
# output：
# r-u-n-o-o-b
# runoob
# >>> students={"name1":"joy","name2":"john","name3":"jerry"}   #连接的序列是字典，会将所有key连接起来
# >>> jn1.join(students)
# 'name1-name2-name3'
# sort 与sorted 区别：
# sort 是应用在list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。 
# list 的sort 方法返回的是对已经存在的列表进行操作，无返回值，
# 而内建函数sorted 方法返回的是一个新的list，而不是在原来的基础上进行的操作。

class Solution:
    def groupAnagrams(self,strs):
        solution = {}
        if len(strs) < 1:
            return strs
        else:
            for i in range(len(strs)): 
                #is in solution,sort完才知道是否有一一对应的关系
                # 记录原始排序
                reg = strs[i]
                regsort = " ".join(sorted(reg))
                if regsort in solution:
                    solution[regsort].append(reg)
                else:
                    #initial a new key group
                    solution[regsort] = [reg]
        return solution.values()              




                   


class Solution:
    def groupAnagrams(self,strs):
        solution = {}
        if len(strs) < 1:
            return strs
        else:
            for i in range(len(strs)): 
                #is in solution,sort完才知道是否有一一对应的关系
                # 记录原始排序
                reg = strs[i]
                regsort = " ".join(sorted(reg))
                if regsort in solution:
                    solution[regsort].append(reg)
                else:
                    #initial a new key group
                    solution[regsort] = [reg]
        return solution.values()             