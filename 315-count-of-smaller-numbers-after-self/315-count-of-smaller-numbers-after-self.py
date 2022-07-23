from bisect import bisect_left
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        nums_sort = []
        for i in reversed(range(len(nums))):
            idx = bisect_left(nums_sort, nums[i])
            nums_sort.insert(idx, nums[i])
            result.append(idx)
        result.reverse()
        return result