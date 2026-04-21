# Day 74 - Phase 3 (DAG DP + Greedy Heap)

## Problems Solved
1. Longest Increasing Path in Matrix (DAG DP)
2. Course Schedule III (Greedy + Heap)

---

## Key Concepts

### 1. DAG DP
- Convert problem into directed acyclic graph
- Use memoized DFS for longest path

### 2. Greedy + Heap
- Sort by constraints
- Remove worst candidate when needed

---

## Key Learnings

- Many grid problems can be modeled as DAGs
- Memoization avoids recomputation in DFS
- Heap helps maintain optimal subset dynamically

---

## Pattern Recognition

- DAG → longest path DP
- Greedy + Heap → scheduling optimization

---

## Complexity

### Problem 1
- Time: O(m * n)
- Space: O(m * n)

### Problem 2
- Time: O(n log n)
- Space: O(n)

---

## Focus Areas

- DAG dynamic programming
- Greedy replacement strategy