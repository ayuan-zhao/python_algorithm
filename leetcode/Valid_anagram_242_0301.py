# -*- coding: utf-8 -*-
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#  anagram not palindrome 字谜不是回文
#不能写 countS[s[i]] = 1+ countS[s[i]],因为当key不存在的时候，会报错
#需要写成 countS[s[i]]= 1 + countS.get(s[i],0),如果有可以就是s[i],没有就返回0
#counting the occurences of each character

class Solution:
    def isAnagram0(self,s:str,t:str):
        if len(s) != len(t):
            return False
        countS,countT = {},{}
        #上一环已经确保长度一样的了
        for i in range(len(s)):
            countS[s[i]] = 1 +countS.get(s[i],0)
           #countT[t[i]]是一个key， 如果字母是一样的，就会在原来的基础上加1
           #给value +1 的方法是countT[t[i]]= 1+countT.get(t[i],0) 
           #get（t[i]）,就是找t[i]这个key的值
            countT[t[i]] = 1+ countT.get(t[i],0)  
            #print("t: ",t,"i: ",i)
            #print("t[i]: ",t[i],"countT[t[i]]: ",countT[t[i]])
        #选一个字符串来遍历， c是String具体的char
        for key in countS:
            #都是在比较value
            if countS[key] != countT.get(key,0):
                return False
        return True   

    def isAnagram1(self,s,t):
        countS,countT = {},{}
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for key in countS:
            if countS[key]  != countT[key]:
                return False
        return True           
            
            



so = Solution()
ia1 = so.isAnagram0(s="elppa",t="apple")
ia2 = so.isAnagram0(s="apple",t="ellpa")

print(ia1)
print(ia2)                   

ia3 = so.isAnagram1(s="elppa",t="apple")
ia4 = so.isAnagram1(s="apple",t="ellpa")

print(ia1)
print(ia2)   