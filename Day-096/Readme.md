# Day 96 - Phase 3 (Eulerian Graph + BFS Path Reconstruction)

## Problems Solved
1. Reconstruct Itinerary (Eulerian Path)
2. Word Ladder II (BFS + Backtracking)

---

## Key Concepts

### 1. Eulerian DFS
- Traverse every edge exactly once
- Build the answer during backtracking

### 2. BFS Path Reconstruction
- Find shortest transformation depth first
- Track parents to rebuild all shortest paths

---

## Key Learnings

- Eulerian traversal helps reconstruct graph routes efficiently
- BFS can be extended to generate all shortest paths
- Parent tracking is essential for path reconstruction problems

---

## Pattern Recognition

- Edge traversal → Eulerian DFS
- Shortest transformation paths → BFS + backtracking

---

## Complexity

### Problem 1
- Time: O(E log E)
- Space: O(E)

### Problem 2
- Time: O(N * 26 * L)
- Space: O(N * L)

---

## Focus Areas

- Graph traversal patterns
- Shortest path reconstruction