# 🧠 Stack & DFS 技巧笔记总结

本页归纳了 Day 2 中涉及的栈结构与 DFS 搜索的核心技巧，便于后续复盘与面试使用。

---

## 📦 栈 Stack

### 📌 适用场景
- 括号匹配（如 LC20）
- 表达式求值（逆波兰表达式）
- 单调栈（如每日温度、接雨水）
- 设计类结构（如 Min Stack）

### 💡 核心技巧
- 使用列表模拟栈：`stack.append(x)`，`stack.pop()`
- 判断匹配时使用哈希映射：`mapping = {')': '('}`
- 配套辅助栈可以同步维护状态（如最小值）

---

## 🌊 DFS（Depth-First Search）

### 📌 适用场景
- 图/网格搜索（如 LC200 岛屿数量）
- 回溯搜索（如组合、排列、数独）
- 树的遍历（先序、中序、后序）

### 💡 核心技巧
- 递归函数写法：
    ```python
    def dfs(x, y):
        if 不合法: return
        标记当前点
        for 四个方向:
            dfs(新位置)
    ```
- 原地修改是减少空间复杂度的好办法：如 `grid[i][j] = '0'`
- 如果系统递归栈报错，可加：
    ```python
    import sys
    sys.setrecursionlimit(10000)
    ```
- 若不想递归，可使用显式栈模拟 DFS：
    ```python
    stack = [(起点)]
    while stack:
        node = stack.pop()
        处理 node
        stack.append(相邻节点)
    ```

---

## 🔁 栈和 DFS 的联系

- 栈是 DFS 的底层结构（无论是系统递归还是手动维护）
- 结构性题目（树、图）都可以通过 DFS 构建解空间
- DFS 更适合搜索全部解（全路径、所有方案）
- 栈更偏向用于状态控制、括号嵌套、表达式求值等

---

## 🧠 思维模板：DFS + 状态标记

```python
visited = set()
def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for neighbor in neighbors(node):
        dfs(neighbor)
