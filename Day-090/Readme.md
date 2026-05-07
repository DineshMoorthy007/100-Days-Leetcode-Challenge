# Day 90 - Phase 3 (Interval DP + Tree Combinatorics)

## Problems Solved
1. Minimum Cost to Cut a Stick (Interval DP)
2. Count Ways to Build Rooms in an Ant Colony (Tree DP + Combinatorics)

---

## Key Concepts

### 1. Interval DP
- Sort cut positions and add boundary points
- Try every possible last cut in a segment
- Use subproblem merging to minimize total cost

### 2. Tree DP + Combinatorics
- Build a rooted tree from parent relationships
- Combine subtree arrangements using combinations
- Count valid construction orders modulo MOD

---

## Key Learnings

- Interval DP is effective when the final action can be chosen inside a segment
- Tree counting problems often combine recursion with combinatorics
- Precomputing factorials makes combination-based DP efficient

---

## Pattern Recognition

- Segment splitting → Interval DP
- Tree construction order counting → Tree DP + Combinatorics

---

## Complexity

### Problem 1
- Time: O(m^3)
- Space: O(m^2)

### Problem 2
- Time: O(n)
- Space: O(n)

---

## Focus Areas

- Interval DP optimization
- Tree DP with combinatorics