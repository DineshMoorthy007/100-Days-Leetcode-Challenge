# Day 92 - Phase 3 (Implicit Graph BFS + Monotonic Queue DP)

## Problems Solved
1. Minimum Genetic Mutation (BFS)
2. Constrained Subsequence Sum (Monotonic Queue DP)

---

## Key Concepts

### 1. Implicit Graph BFS
- Treat transformations as graph edges
- BFS ensures shortest mutation sequence

### 2. Monotonic Queue DP
- Track maximum DP values efficiently
- Optimize sliding-window transitions

---

## Key Learnings

- Many transformation problems form implicit graphs
- BFS works well for minimum-step problems
- Monotonic deque drastically reduces DP complexity

---

## Pattern Recognition

- String transformations → BFS
- Window DP → monotonic deque

---

## Complexity

### Problem 1
- Time: O(8 * 4 * n)
- Space: O(n)

### Problem 2
- Time: O(n)
- Space: O(n)

---

## Focus Areas

- Implicit graph traversal
- Sliding-window DP optimization