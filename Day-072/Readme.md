# Day 72 - Phase 3 (Weighted String DP + Graph DP)

## Problems Solved
1. Minimum ASCII Delete Sum for Two Strings (String DP)
2. Number of Restricted Paths (Graph + DP)

---

## Key Concepts

### 1. Weighted Edit Distance
- Minimize cost instead of operations
- Use ASCII values for transitions

### 2. Graph + DP Hybrid
- Compute shortest distances first
- Apply DP on valid monotonic paths

---

## Key Learnings

- Edit distance variants often involve weights
- Precomputing shortest paths simplifies DP
- Constraints define valid transitions in graph DP

---

## Pattern Recognition

- String DP → cost-based transformation
- Graph + monotonic constraint → DFS + memo

---

## Complexity

### Problem 1
- Time: O(m * n)
- Space: O(m * n)

### Problem 2
- Time: O(E log V)
- Space: O(V + E)

---

## Focus Areas

- String DP variations
- Graph + DP integration