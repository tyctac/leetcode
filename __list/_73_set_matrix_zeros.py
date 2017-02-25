class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        has_zeros_row = False
        has_zeros_col = False
        m = len(matrix)
        n = len(matrix[0])
        for j in range(n):
            if matrix[0][j] == 0:
                has_zeros_row = True

        for i in range(m):
            if matrix[i][0] == 0:
                has_zeros_col = True

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] =0
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if has_zeros_row:
            for j in range(n):
                matrix[0][j] = 0
        if has_zeros_col:
            for i in range(m):
                matrix[i][0] = 0

so = Solution()
matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
so.setZeroes(matrix)
print matrix

