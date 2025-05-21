class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        sol=[]

        for i in range(m):
            lst=[]
            for j in range(n-1,-1,-1):
                lst.append(matrix[j][i])
            sol.append(lst)

        for p in range(m):
            for q in range(n):
                matrix[p][q]=sol[p][q]
        return matrix


        