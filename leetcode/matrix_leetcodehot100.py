#73矩阵置零
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])  # 得到矩阵的行和列数
        first_row_zero = False
        # 检查第一行是否含有零
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        first_col_zero = False
        # 检查第一列是否含有零
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # 标记第i行和第j列，这里是不是0开始无所谓，但是下一步一定要1开始
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # 标记第i行的第0 列=0
                    matrix[0][j] = 0  # 标记第j列

        # 使用标记修改矩阵
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                # 修改第0行和第0列必须放在最后
        # 修改第一行
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # 修改第一列
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
