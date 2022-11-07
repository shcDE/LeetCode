class Solution:
    def maximum69Number (self, num: int) -> int:
        n = list(str(num))
        i = 0
        
        while i < len(n):
            if n[i] == '6':
                n[i] = '9'
                break
            elif n[i] == '9':
                i += 1
                
        return ''.join(n)