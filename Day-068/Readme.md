# Day 68 - Phase 3 (Interval DP + Tree DP)

## Problems Solved
1. Minimum Cost to Merge Stones (Interval DP)
2. Binary Tree Maximum Path Sum (Tree DP)

---

## Key Concepts

### 1. Interval DP
- Solve over subarrays
- Try valid partitions
- Add merge cost conditionally

### 2. DP on Trees
- Return best path ending at node
- Maintain global answer for split paths

---

## Key Learnings

- Interval DP requires careful partition constraints
- Tree DP separates local return vs global update
- Not all subproblems are valid (important pruning)

---

## Pattern Recognition

- Interval DP → Merge / partition problems
- Tree DP → Path-based optimization

---

## Complexity

### Problem 1
- Time: O(n^3 / K)
- Space: O(n^2)

### Problem 2
- Time: O(n)
- Space: O(h)

---

## Focus Areas

- Hard interval DP
- Tree-based dynamic programming