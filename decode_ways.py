class Solution:
    """ https://leetcode.com/problems/decode-ways/ """
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        elif int(s[0:2]) <= 26:
            return self.numDecodings(s[2:]) + self.numDecodings(s[1:])
        else:
            return 1 + self.numDecodings(s[1:])
