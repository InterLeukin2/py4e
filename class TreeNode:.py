class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
breakpoint()
# 补充 build_tree 函数，用来从列表构建二叉树
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])  # 创建根节点
    queue = [root]  # 使用队列按层次创建树
    i = 1  # 从第二个元素开始
    while i < len(values):
        node = queue.pop(0)  # 取出队列的第一个节点
        if i < len(values):  # 构建左子树
            node.left = TreeNode(values[i])
            queue.append(node.left)
            i += 1
        if i < len(values):  # 构建右子树
            node.right = TreeNode(values[i])
            queue.append(node.right)
            i += 1
    return root

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)        # Step 1: Traverse left subtree
            result.append(node.val)  # Step 2: Visit the root node
            dfs(node.right)       # Step 3: Traverse right subtree

        result = []
        dfs(root)
        return result

# 给定列表
n = [1, 2, 3, 4, 5, 6, 7]

# 使用 build_tree 函数构建树
root = build_tree(n)  # 构建树

# 创建 Solution 类实例并调用方法
solution = Solution()
result = solution.inorderTraversal(root)  # 传入构建的树的根节点
print(result)  # 打印结果