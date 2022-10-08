class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = diff = float("inf")
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                sums = nums[i]+nums[l]+nums[r]
                if abs(sums-target) < diff:
                    diff, answer = abs(sums-target), sums
                if sums < target: 
                    l += 1
                elif sums > target:
                    r -= 1
                else:
                    return answer
        return answer
        
        