class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        data = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if (i-j) not in data.keys():
                    data[i-j] = [mat[i][j]]
                else:
                    data[i-j].append(mat[i][j])
                    
        for i in sorted(data.keys()):
            data[i] = sorted(data[i], reverse=True)
            
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mat[i][j] = data[i-j].pop()
                
        return mat