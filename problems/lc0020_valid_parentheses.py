# LC 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False  # invalid character (for safety)

        return not stack  # stack should be empty at the end

# ✅ Time: O(n), Space: O(n)
# 🎯 技巧：利用栈记录未匹配的左括号，右括号检查并弹出
