import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        k = len(words[0])
        answer = []
        
        for l in range(k):
            d = collections.Counter(words)
            for r in range(l + k, len(s) + 1, k):
                word = s[r - k: r]
                d[word] -= 1
                
                while d[word] < 0:
                    d[s[l:l + k]] += 1
                    l += k
                
                if l + k * len(words) == r:
                    answer.append(l)
        
        return answer