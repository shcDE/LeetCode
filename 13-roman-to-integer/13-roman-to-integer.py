class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        dic2 = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        
        answer = 0
        
        for i, j in enumerate(s):
            if j in dic and (s[i:i+2])in dic2:
                answer -= dic[j]
            else:
                answer += dic[j]
        return answer