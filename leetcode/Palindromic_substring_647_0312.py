class Solution:
    def Palindromic_substring(self, s):
        res = 0
        # get odd length palindromes
        for i in range(len(s)):
            left = right = i
            # s[left] == s[right] means found a palindromic
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            #get even length palindromes    
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res

    