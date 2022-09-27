class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = list('*' + dominoes + '*')
        stack = []
        def push(l, r, n):
            if r - l <= 1:
                return n
            if r-l == 2:
                if n[r]+n[l] in ('RL', 'LR'):
                    return n
            go = False
            if n[l] == 'R':
                n[l+1] = 'R'
                l += 1
                go = True
            if n[r] == 'L':
                n[r-1] = 'L'
                r -= 1
                go = True
            if go:
                return push(l,r,n)
            return n
        for i in range(len(n)):
            if n[i] != '.':
                if stack != []:
                    n = push(stack[-1], i, n)
                stack.append(i)
        return ''.join(n[1:len(n)-1])