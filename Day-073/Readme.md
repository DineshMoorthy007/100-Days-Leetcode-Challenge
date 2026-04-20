# Day 73 - Phase 3 (Tree DP + BFS State)

## Problems Solved
1. Maximum Sum BST in Binary Tree (Tree DP)
2. Shortest Path to Get All Keys (BFS + Bitmask)

---

## Key Concepts

### 1. Tree DP
- Return multiple values from recursion
- Validate conditions bottom-up

### 2. BFS with State
- Combine position + collected keys
- Avoid revisiting same state

---

## Key Learnings

- Tree problems often require structured return values
- BFS state should include all changing variables
- Validation + DP often go together in tree problems

---

## Pattern Recognition

- Tree DP → postorder with multi-state return
- BFS + Bitmask → grid constraint problems

---

## Complexity

### Problem 1
- Time: O(n)
- Space: O(h)

### Problem 2
- Time: O(m * n * 2^k)
- Space: O(m * n * 2^k)

---

## Focus Areas

- DP on trees
- BFS state optimization