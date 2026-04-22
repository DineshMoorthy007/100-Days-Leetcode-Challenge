# Day 75 - Phase 3 (Greedy Expansion + Bitmask DP)

## Problems Solved
1. Maximum Score of a Good Subarray (Greedy)
2. Maximum Students Taking Exam (Bitmask DP)

---

## Key Concepts

### 1. Greedy Expansion
- Expand around fixed index
- Maintain minimum dynamically

### 2. Bitmask DP
- Encode states efficiently
- Handle adjacency constraints

---

## Key Learnings

- Greedy works when expansion decisions are locally optimal
- Maintaining constraints during expansion is key
- Bitmask DP helps manage complex state transitions

---

## Pattern Recognition

- Fixed index constraint → expand window
- Grid constraint → bitmask DP

---

## Complexity

### Problem 1
- Time: O(n)
- Space: O(1)

### Problem 2
- Time: O(m * 2^n * 2^n)
- Space: O(m * 2^n)

---

## Focus Areas

- Greedy expansion strategies
- State compression DP