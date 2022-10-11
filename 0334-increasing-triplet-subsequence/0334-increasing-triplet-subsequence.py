class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a,b = float("inf"), float("inf")
        for element in nums:
            if element <= a:
                a = element
            elif element<= b:
                b = element
            else:
                return True
        return False