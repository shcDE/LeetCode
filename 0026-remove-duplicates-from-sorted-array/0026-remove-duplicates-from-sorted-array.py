class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for item in sorted(list(set(nums))):
            nums[k] = item
            k += 1
        return k