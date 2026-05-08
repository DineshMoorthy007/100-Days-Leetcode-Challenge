# Day 91 - Phase 3 (Memoized DP + 3D State DP)

## Problems Solved
1. Minimum Number of Days to Eat N Oranges (Recursion + Memoization)
2. Paint House III (3D DP)

---

## Key Concepts

### 1. Memoized Reduction DP
- Reduce the state using optimal operations
- Cache overlapping recursive states

### 2. Multi-State DP
- Track index, previous color, and neighborhood count
- Transition carefully across constrained states

---

## Key Learnings

- Memoization significantly reduces repeated recursion
- State-heavy problems require careful transition modeling
- Multi-dimensional DP improves constraint handling

---

## Pattern Recognition

- Integer reduction → memoized recursion
- Constraint optimization → multi-state DP

---

## Complexity

### Problem 1
- Time: O(log² n)
- Space: O(log n)

### Problem 2
- Time: O(m * n² * target)
- Space: O(m * n * target)

---

## Focus Areas

- Memoized recursion
- Multi-dimensional DP