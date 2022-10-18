class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = '11'
        for i in range(n-2):
            c, t = 1, ''
            for j in range(len(s)-1):
                if s[j+1] == s[j]:
                    c += 1
                else:
                    t += str(c)+s[j]
                    c = 1
            if s[-2] == s[-1]:
                t += str(c) + s[-1]
            else:
                t += '1'+s[-1]
            s = t
            
        return s