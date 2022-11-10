##def transpose(matrix):
##    mat = []
##    n = len(matrix)
##    m = len(matrix[0])
##    for i in range(n):
##        for j in range(m):
##            mat[i][j] = matrix[j][i]
##    matrix = mat
            
            
def transpose(matr):
    res=[]
    n=len(matr)
    m=len(matr[0])
    for j in range(m):
        tmp=[]
        for i in range(n):
            tmp=tmp+[matr[i][j]]
        res=res+[tmp]
    matr = res        


matrix = [[1]]
transpose(matrix)
for line in matrix:
    print(*line)

matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)
