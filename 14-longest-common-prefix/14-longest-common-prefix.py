class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        minimum = min(strs, key=len)
        for i, ch in enumerate(minimum):
            for j in strs:
                if j[i] != ch:
                    return minimum[:i]
        return minimum 