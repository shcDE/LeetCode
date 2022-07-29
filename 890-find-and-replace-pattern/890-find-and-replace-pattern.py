class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        target = len(set(pattern))
        def evaluate(word):
            return len(set(word)) == len(set(zip(pattern, word))) == target
        return list(filter(evaluate, words))
