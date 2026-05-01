# Day 84 - Phase 3 (Grid DP + Bidirectional BFS)

## Problems Solved
1. Cherry Pickup II (Grid DP)
2. Word Ladder (Bidirectional BFS)

---

## Key Concepts

### 1. Multi-Agent DP
- Track multiple positions
- Avoid duplicate counting

### 2. Bidirectional BFS
- Search from both ends
- Meet in the middle

---

## Key Learnings

- Multi-agent DP increases state complexity
- Bidirectional BFS reduces search space drastically
- Choosing the smaller frontier improves efficiency

---

## Pattern Recognition

- Grid DP → multi-state transitions
- Graph → meet-in-the-middle BFS

---

## Complexity

### Problem 1
- Time: O(m * n^2)
- Space: O(m * n^2)

### Problem 2
- Time: O(N * 26 * L)
- Space: O(N)

---

## Focus Areas

- Grid DP
- Bidirectional BFS