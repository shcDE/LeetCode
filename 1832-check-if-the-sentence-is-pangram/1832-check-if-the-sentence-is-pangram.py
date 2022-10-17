class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        sentence = list(sentence)
        i = 0
        while i != len(alphabet):
            if alphabet[i] not in sentence:
                return False
                break
            else:
                i += 1
                
        return True
                