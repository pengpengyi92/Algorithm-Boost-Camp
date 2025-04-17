# 📅 Day 01 - 2025/04/17 | Array + Hash Table 专项训练

## 🔍 今日目标

- 热身题 + 高频数组题型巩固
- 掌握 Hash + Set 的查找技巧
- 熟悉双指针原地覆盖写法
- 提升代码规范性与注释能力

---

## 🧠 刷题记录

### 1. LC0001 Two Sum
- **思路**：使用哈希表记录访问过的数字位置，查找当前数字所需补数是否存在。
- **时间复杂度**：O(n)
- **关键词**：Hash Table、查找补数
- **代码见**：[`problems/lc0001_two_sum.py`](../problems/lc0001_two_sum.py)

---

### 2. LC0026 Remove Duplicates from Sorted Array
- **思路**：双指针遍历数组，只在发现不同元素时覆盖前指针位置。
- **空间限制**：原地修改，不能额外开空间。
- **关键词**：双指针、覆盖写法、排序数组
- **代码见**：[`problems/lc0026_remove_duplicates.py`](../problems/lc0026_remove_duplicates.py)

---

### 3. LC0128 Longest Consecutive Sequence
- **思路**：先转为 `set`，从每个可能的连续起点出发，向右扩展。
- **技巧**：起点判定用 `num - 1 not in set` 节省多余计算。
- **关键词**：HashSet、去重、O(n) 优化
- **代码见**：[`problems/lc0128_longest_consecutive.py`](../problems/lc0128_longest_consecutive.py)

---

## ✨ 总结笔记

- Hash 是查找类问题的核心技巧，避免暴力 O(n²)
- 排序数组题可以考虑双指针优化空间复杂度
- `set` 在去重和 O(1) 查找中非常强大
- 题目理解和变量命名要规范，为复习留好注释

---

## ✅ 今日成就

| 题目编号 | 标题                         | 状态   |
|----------|------------------------------|--------|
| LC0001   | Two Sum                      | ✅ Done |
| LC0026   | Remove Duplicates            | ✅ Done |
| LC0128   | Longest Consecutive Sequence | ✅ Done |

🧱 “每天一小时，一步步登顶量化之巅。”

