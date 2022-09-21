class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sums = sum(a for a in nums if a%2 == 0)
        for i in range(len(queries)):
            val, ind = queries[i]
            sums -= nums[ind]%2 == 0 and nums[ind]
            nums[ind] += val
            sums += nums[ind]%2 == 0 and nums[ind]
            queries[i] = sums
            
        return queries