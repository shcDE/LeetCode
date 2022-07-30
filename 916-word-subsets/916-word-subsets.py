from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w2Counter = Counter()
        for w2 in words2:
            w2Counter |= Counter(w2)
        
        return {w1 for w1 in words1 if w2Counter == w2Counter&Counter(w1)}
    