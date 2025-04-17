# LC 1. Two Sum
# Problem link: https://leetcode.com/problems/two-sum/
# Tags: Array, Hash Table
# Difficulty: Easy

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], i]
            hash_map[num] = i

# ✅ Complexity:
# Time: O(n)
# Space: O(n)

# ✅ Notes:
# - 使用哈希表记录已访问元素，快速查找补数是否存在。
