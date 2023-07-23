class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        freq1 = [0 for i in range(26)]
        freq2 = [0 for i in range(26)]

        for c in s:
            freq1[ord(c)-97]+=1
        for c in t:
            freq2[ord(c)-97]+=1
        
        return True if freq1 == freq2 else False
