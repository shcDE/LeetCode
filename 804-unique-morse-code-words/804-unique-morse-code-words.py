class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        output_list = set()
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        trans_list = []
        
        for word in words:
            current = []
            for char in word:
                current.append(morse[ord(char) - ord('a')])
            if ''.join(current) not in trans_list:
                trans_list.append(''.join(current))
        
        return(len(trans_list))