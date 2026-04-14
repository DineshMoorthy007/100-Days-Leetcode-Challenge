# Day 67 - Phase 3 (Digit DP + 0-1 BFS)

## Problems Solved
1. Numbers At Most N Given Digit Set (Digit DP)
2. Minimum Cost to Make at Least One Valid Path in a Grid (0-1 BFS)

---

## Key Concepts

### 1. Digit DP
- Build numbers under constraints
- Tight flag controls upper bound

### 2. 0-1 BFS
- Use deque for binary weights
- Push front for cost 0, back for cost 1

---

## Key Learnings

- Digit DP helps solve counting under limits
- 0-1 BFS is more optimal than Dijkstra for binary weights
- Recognizing edge weight patterns is crucial

---

## Pattern Recognition

- Digit DP → Counting problems
- Graph (0/1 weights) → 0-1 BFS

---

## Complexity

### Problem 1
- Time: O(len(n) * digits)
- Space: O(len(n))

### Problem 2
- Time: O(m * n)
- Space: O(m * n)

---

## Focus Areas

- Digit DP mastery
- Graph optimization techniques