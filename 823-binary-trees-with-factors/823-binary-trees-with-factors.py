import collections

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        cnt = 0
        dp = collections.Counter()
        for i,num in enumerate(arr):
            dp[num] = 1
            for j in range(i):
                if num % arr[j] == 0:
                    dp[num] += dp[arr[j]] * dp[num/arr[j]]
            cnt += dp[num]
        return cnt % (10**9 + 7)