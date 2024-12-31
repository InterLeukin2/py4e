'''
200.岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

'''

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0]) #这里len天然多1，所以后面不用在意循环时的边界问题

#step 2
        def dfs(i, j):
            # 如果超出边界或是水（'0'），则返回
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == '0':
                return #当 return 被触发时，dfs 函数将退出当前的递归路径，
                        # 返回到调用这个 dfs(i, j) 的上一层调用中
                        # ，继续执行其他的逻辑或递归调用。
            # 标记当前陆地为已访问
            grid[i][j] = '0'
            # 向四个方向扩展（上下左右），这几步换顺序也是可以的吧，因为每次执行下一步都是从上一步的递归开始
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        island_count = 0 #这里也可以从一开始初始化
#step 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':  # 如果是陆地，注意这里是字符，是根据题意
                    island_count += 1  # 新岛屿，岛屿数量加一
                    dfs(i, j)  # 启动 DFS，标记该岛屿

        return island_count