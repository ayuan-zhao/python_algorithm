# -*- coding: utf-8 -*-
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets. []{[]
# Open brackets must be closed in the correct order. for example : ({)} is not in a correct order
# 先读入，看看是不是一对，用dictionary
class Solution:
    def isValid(self, s):

        stack = []
        lookup = {"(": ")", "[": "]", "{": "}"}
        for parenthese in s:
            # 找这个key，是不是存在,{[]},前两个符号会被append,下一步再判断是不是 in order
            # 比如{[]}，要求"]”的上一步，stack最top是一个方括号
            if parenthese in lookup:
                stack.append(parenthese)
                # 用len(stack)来测试，string只有一边括号的情况，s = "]"/"]})"
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        # 最后去判断 “s"是否为空
        return len(stack) == 0

    def isValid0(self, s):
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False                


so = Solution()
ans = so.isValid0("[[{{}}]}")
ans0 = so.isValid0("[[{{}}]]")
ans1 = so.isValid0("[[{{}}]」")
ans2 = so.isValid0("[")
ans3 = so.isValid0("]")
ans4 = so.isValid0("")

print(ans, ans0, ans1, ans2, ans3, ans4)

ans = so.isValid0("[[{{}}]}")
ans0 = so.isValid("[[{{}}]]")
ans1 = so.isValid("[[{{}}]」")
ans2 = so.isValid("[")
ans3 = so.isValid("]")
ans4 = so.isValid("")

print(ans, ans0, ans1, ans2, ans3, ans4)
