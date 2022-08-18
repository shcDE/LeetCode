from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l, result = len(arr), 0
        for element, cnt in Counter(arr).most_common():
            l -= cnt
            result += 1
            if l <= len(arr)//2:
                return result
        