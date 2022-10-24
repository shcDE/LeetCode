class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def back_track(i, curr):
            if i == len(arr):
                self.result = max(self.result, len(curr))
                return
            if len(set(arr[i])) == len(arr[i]):
                if all(c not in curr for c in arr[i]):
                    back_track(i+1, curr+arr[i])
                    
            back_track(i+1, curr)
            
        self.result = 0
        back_track(0, '')
        return self.result