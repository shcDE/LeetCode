from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        c = Counter(words)
        d = sorted(c.items(), key=lambda x: x[1], reverse=True)
        
        return [d[i][0] for i in range(k)]
        