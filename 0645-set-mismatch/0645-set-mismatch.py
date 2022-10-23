from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        ctr = Counter(nums)
        for key, value in ctr.items():
            if value == 2:
                result.append(key)
                break
        result.append(sum(range(1,len(nums)+1))-(sum(nums)-result[0]))
        return result
        