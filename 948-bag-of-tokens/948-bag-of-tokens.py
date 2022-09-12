from collections import deque

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        queue = deque(tokens)
        
        result = score = 0
        
        while queue:
            if score < 0:
                break
                
            if power >= queue[0]:
                score += 1
                result = max(score, result)
                power -= queue.popleft()
                
            else:
                score -= 1
                power += queue.pop()
                
        return result