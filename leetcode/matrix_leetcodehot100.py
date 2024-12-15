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
#48旋转图像
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        for i in range(n):
            for j in range(i + 1, n):  # Only consider the upper triangle，这个写法能限制  j > i ：
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

#先转置，再反转行，对角线不变，为什么这个限制有效：

"""	代码中确实限制了  j > i ，通过 for j in range(i + 1, n) 这一行实现的：
1.	避免重复交换
	•	例如，交换 matrix[0][1] 和 matrix[1][0] 时，如果没有限制  j > i ，那么在外层  i = 1 、内层  j = 0  时，又会重复交换回来。
	2.	避免下三角部分访问
	•	range(i + 1, n) 直接跳过对角线和下三角部分。
	•	下三角部分对称于上三角部分，所以没必要访问。"""
#假设问旋转180度怎么做：
#1，转2次90
class Solution:
    def rotate90(self, matrix: List[List[int]]) -> None:
        """
        Helper function to rotate the matrix 90 degrees clockwise.
        """
        n = len(matrix)
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

    def rotate180(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix 180 degrees by calling rotate90 twice.
        """
        self.rotate90(matrix)  # First 90-degree rotation
        self.rotate90(matrix)  # Second 90-degree rotation
#方法2.上下翻转，左右翻转
class Solution:
    def rotate180(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Rotate the matrix 180 degrees clockwise.
        """
        # 上下翻转
        matrix.reverse()

        # 每一行左右翻转
        for row in matrix:
            row.reverse()
#240 搜索二维矩阵
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1  # 从右上角开始

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # 如果当前元素大于目标，向左移动
            else:
                row += 1  # 如果当前元素小于目标，向下移动

        return False  # 没有找到目标，返回 False
