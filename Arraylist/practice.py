class Solution:
    def isValid(self,s):
        stack = []
        parenthesedict = {"[":"]","{":"}","(":")"}
        for parenthese in s:
            if parenthese in parenthesedict:
                stack.append(parenthese) 
            elif len(stack) ==0 or parenthesedict[stack.pop()]!= parenthese:
                return False
        return len(stack) == 0               


       

so = Solution() 
ans0 = so.isValid("[[{{}}]]")      
ans1 = so.isValid("[[{{}}][[")
ans2 = so.isValid("[")
ans3 = so.isValid("]")
ans4 = so.isValid("")


print(ans0, ans1, ans2, ans3, ans4)