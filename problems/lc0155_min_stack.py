# LC 155. Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  # 同步记录每一层的最小值

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 同步 push 当前最小值
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# ✅ Time: O(1) for all operations
# ✅ Space: O(n) for extra min_stack
# 🎯 技巧：设计类时保持状态同步是关键。每步都维护最小值。
