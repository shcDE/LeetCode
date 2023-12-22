class Solution:
    def maxScore(self, s: str) -> int:
        s = list(s)
        result = 0
        for i in range(len(s)):
            zeros, ones = 0, 0
            if len(s[:i+1]) != 0 and len(s[i+1:]) != 0:
                if "0" in s[:i+1]:
                    zeros += s[:i+1].count("0")
                if "1" in s[i+1:]:
                    ones += s[i+1:].count("1")
                result = max(result, zeros + ones)         
        return result