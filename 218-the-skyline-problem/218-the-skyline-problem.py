# 디스커션 클론함

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        li, queue, result, removed = [], [0], [], defaultdict(int)
        for l,r,h in buildings:
            li.extend([[l, -h], [r, h]])
        li.sort()
        for pos, v in li:
            cur = queue[0]
            if v<0:
                heappush(queue, v)
            else:
                removed[v]+=1
            while removed[-queue[0]]:
                removed[-queue[0]]-=1
                heappop(queue)
            if queue[0]!=cur:
                result.append([pos, -queue[0]])
        return result