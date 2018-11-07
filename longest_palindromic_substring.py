#!/usr/bin/env python3

#Given a string s, find the longest palindromic substring in s. 
#You may assume that the maximum length of s is 1000.

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return ''
        if len(s) == 1:
            return s
        start = 0
        end = 0
        max_len = 0
        max_str = ''
        for i in range(len(s)):
            l1 = self.extendleftright(s, i, i)
            l2 = self.extendleftright(s, i, i+1)
            max_len = max(l1, l2)
            if max_len > end - start:
                if max_len%2 == 0:
                    start = i-max_len//2+1
                    end = i+max_len//2
                else:
                    start = i-max_len//2
                    end = i+max_len//2
        return s[start:end+1]
    
    
    def extendleftright(self, s, left, right):
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l]==s[r]:
            l = l-1
            r = r+1
            
        return r-1-l
        
