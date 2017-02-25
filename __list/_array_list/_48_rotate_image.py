class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        if l%2 == 0:
            t = l/2
            l = l-1
            for a in range(0,t):
                print 'ok'
                for b in range(0,t):
                    tmp = matrix[a][b]
                    matrix[a][b] = matrix[l-b][a]
                    matrix[l-b][a] = matrix[l-a][l-b]
                    matrix[l-a][l-b] = matrix[b][l-a]
                    matrix[b][l-a] = tmp
        else:
            t = l/2
            l = l-1
            for a in range(0,t):
                print 'ok'
                for b in range(0,t):
                    tmp = matrix[a][b]
                    matrix[a][b] = matrix[l-b][a]
                    matrix[l-b][a] = matrix[l-a][l-b]
                    matrix[l-a][l-b] = matrix[b][l-a]
                    matrix[b][l-a] = tmp
            a = t
            for b in range(0,t):
                tmp = matrix[a][b]
                matrix[a][b] = matrix[l-b][a]
                matrix[l-b][a] = matrix[l-a][l-b]
                matrix[l-a][l-b] = matrix[b][l-a]
                matrix[b][l-a] = tmp

so = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
so.rotate(matrix)
print matrix
