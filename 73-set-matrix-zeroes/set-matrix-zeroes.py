class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    lst.append([i,j])

        for iter in (lst):
            i=iter[0]
            j=iter[1]
            for k in range(m):
                matrix[k][j]=0

            for l in range(n):
                matrix[i][l]=0
        return matrix
        