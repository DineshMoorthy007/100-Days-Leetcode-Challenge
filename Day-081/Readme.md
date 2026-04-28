# Day 81 - Phase 3 (Knapsack Variant + BFS State)

## Problems Solved
1. Tallest Billboard (Knapsack DP)
2. Shortest Path with Obstacles (BFS + State)

---

## Key Concepts

### 1. Difference DP
- Track difference instead of sum
- Optimize partition problems

### 2. BFS with State
- Include extra dimension (remaining eliminations)
- Avoid revisiting states

---

## Key Learnings

- Knapsack problems can be transformed using difference states
- BFS can handle multiple constraints using state tracking
- State explosion must be controlled carefully

---

## Pattern Recognition

- Partition problems → difference DP
- Grid + constraints → BFS with state

---

## Complexity

### Problem 1
- Time: O(n * sum)
- Space: O(sum)

### Problem 2
- Time: O(m * n * k)
- Space: O(m * n * k)

---

## Focus Areas

- Knapsack variants
- BFS with multi-state