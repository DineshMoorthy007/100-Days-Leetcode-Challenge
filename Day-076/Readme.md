# Day 76 - Phase 3 (Trie + Sliding Window)

## Problems Solved
1. Word Search II (Trie + DFS)
2. Minimum Window Substring (Sliding Window)

---

## Key Concepts

### 1. Trie + Backtracking
- Prefix pruning reduces search space
- Combine DFS with Trie traversal

### 2. Sliding Window
- Maintain valid window dynamically
- Expand + shrink strategy

---

## Key Learnings

- Trie drastically improves multi-word search
- Backtracking must be optimized with pruning
- Sliding window requires careful validity tracking

---

## Pattern Recognition

- Trie + DFS → word search problems
- Sliding window → substring optimization

---

## Complexity

### Problem 1
- Time: O(m * n * 4^L)
- Space: O(total characters in Trie)

### Problem 2
- Time: O(n)
- Space: O(k)

---

## Focus Areas

- Trie + backtracking
- Advanced sliding window