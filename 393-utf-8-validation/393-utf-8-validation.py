class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0
        
        for byte in data:
            if byte >= 128 and byte <= 191:
                if not cnt:
                    return False
                cnt -= 1
            else:
                if cnt:
                    return False
                if byte < 128:
                    continue
                elif byte < 224:
                    cnt = 1
                elif byte < 240:
                    cnt = 2
                elif byte < 248:
                    cnt = 3
                else:
                    return False
        
        return cnt == 0