# LC 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # 只有起点才进入循环，节省时间
            if num - 1 not in num_set:
                current = num
                streak = 1
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                longest = max(longest, streak)

        return longest

# ✅ Time: O(n), Space: O(n)
# 🎯 技巧：用 set 判定连续起点，避免重复遍历
