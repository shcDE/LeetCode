class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pig = 0
        while (minutesToTest / minutesToDie + 1)**pig < buckets:
            pig += 1
        return pig