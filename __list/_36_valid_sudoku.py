class Solution(object):

    def tranverse(self,board):
        l = len(board)
        bd = []
        for i in board:
            tmpl = []
            for j in i:
                if j == '.':
                    tmpl.append(0)
                else:
                    tmpl.append((int)(j))
            bd.append(tmpl)
        return bd

    def anti_tranverse(self,bd):
        l = len(bd)
        board = []
        for i in bd:
            tmpl = []
            for j in i:
                if j ==0:
                    tmpl.append('.')
                else:
                    tmpl.append(str(j))
            board.append(tmpl)
        return board

    def judge_one(self,i,j,bd):
        flag = False
        x = bd[i][j]
        set_row = set()
        for p in range(9):
            if bd[i][p] == '.':
                continue
            if bd[i][p] in set_row:
                return False
            else:
                set_row.add(bd[i][p])
        set_col = set()
        for p in range(9):
            if bd[p][j] == '.':
                continue
            if bd[p][j] in set_col:
                return False
            else:
                set_col.add(bd[p][j])
        set_box = set()
        base_row = i/3
        base_col = j/3
        for p in range(3):
            for q in range(3):
                if bd[base_row*3+p][base_col*3+q] == '.':
                    continue
                if bd[base_row*3+p][base_col*3+q] in set_box:
                    return False
                else:
                    set_box.add(bd[base_row*3+p][base_col*3+q])


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # bd = self.tranverse(board)
        lens = 9
        for i in range(9):
            for j in range(9):
                if i == 6 and j == 6:
                    print 'ooo'
                if board[i][j] == '.':
                    continue
                f = self.judge_one(i,j,board)
                if f == False:
                    return False

        return True

so = Solution()
board = [".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."]
print so.isValidSudoku(board)