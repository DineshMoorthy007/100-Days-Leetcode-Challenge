# Day 88 - Phase 3 (Bitmask DP + Subset Optimization)

## Problems Solved
1. Minimum XOR Sum of Two Arrays (Bitmask DP)
2. Maximum Score Words Formed by Letters (Backtracking)

---

## Key Concepts

### 1. Bitmask DP (Assignment)
- Encode assignments using mask
- Map mask bits → index

### 2. Subset Backtracking
- Include/exclude decisions
- Prune invalid states early

---

## Key Learnings

- Bitmask DP efficiently solves assignment problems
- Counting bits helps derive state transitions
- Backtracking requires strong pruning to scale

---

## Pattern Recognition

- Assignment → bitmask DP
- Subset → backtracking / DP

---

## Complexity

### Problem 1
- Time: O(n * 2^n)
- Space: O(2^n)

### Problem 2
- Time: O(2^n)
- Space: O(n)

---

## Focus Areas

- Bitmask DP
- Subset optimization