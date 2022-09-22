class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = list(s.split(" "))
        strr = ''
        s_rev = ''
        for i in range(len(s_list)):
            for j in range(len(s_list[i])):
                s_rev += s_list[i][-1-j]
            s_rev += " "
        
        strr+= s_rev
            
        return strr[:-1]