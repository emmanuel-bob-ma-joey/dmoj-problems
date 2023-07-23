import string;
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(ch for ch in s if ch.isalnum())

        s = s.replace(" ","")
        s = s.lower()
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
    

    



