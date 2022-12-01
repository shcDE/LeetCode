class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        l = len(s)//2
        a, b = s[:l], s[l:]
        aC, bC = 0, 0
        
        for i in range(l):
            if a[i] in vowels: 
                aC += 1
            if b[i] in vowels: 
                bC += 1
        
        return aC == bC