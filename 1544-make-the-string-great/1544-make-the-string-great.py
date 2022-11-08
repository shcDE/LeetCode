from collections import deque

class Solution:
    def makeGood(self, s: str) -> str:
        s, stack, is_good = deque(s), [], False
        
        while not is_good:
            is_good = True
            
            while s:
                curr = s.popleft()
                if stack and stack[-1] == curr.swapcase():
                    is_good = False
                    stack.pop()
                else:
                    stack.append(curr)
                    
        return ''.join(stack)