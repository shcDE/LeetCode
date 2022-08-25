class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = 0
        ransomeNote = list(ransomNote)
        magazine = list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine.remove(ransomeNote[i])
                cnt += 1
        
        if cnt == len(ransomNote):
            return True
        else:
            return False