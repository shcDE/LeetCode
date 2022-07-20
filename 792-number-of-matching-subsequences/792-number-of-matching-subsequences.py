class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cnt = 0
        word_list = defaultdict(list)
        for word in words:
            word_list[word[0]].append(word)
        for char in s:
            if char not in word_list:
                continue
            for word in word_list.pop(char):
                if len(word) == 1:
                    cnt += 1
                else:
                    word_list[word[1]].append(word[1:])
        return cnt