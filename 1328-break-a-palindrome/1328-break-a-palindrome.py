class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        i = 0
        
        while i < (len(palindrome)-1)/2:
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
            i += 1
        return palindrome[:-1] + 'b'