#sliding window  
from email import charset


class Solution:    
    def lengthOfLongestSubstring(self,s):
        charSet = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in charset:
                charSet . remove(s[left])
                left += 1
            charSet .add(s[left])  
            # 
            res = max(res,right - left +1)
        return res     


    def lengthOfLongestSubstring1(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            if s[r] not in seen:
                output = max(output,r-l+1)
         
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            #key:char,value: last indexing 
            # update right point       
            seen[s[r]] = r
        return output
           
            #There are two cases if s[r] in seen:
            #case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            #case2: s[r] is not inside the current window, we can keep increase the window
         