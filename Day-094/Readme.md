# Day 94 - Phase 3 (DP Transformation + Greedy Heap)

## Problems Solved
1. Delete and Earn (DP Transformation)
2. Minimum Cost to Hire K Workers (Greedy + Heap)

---

## Key Concepts

### 1. DP Transformation
- Convert the problem into House Robber pattern
- Handle adjacency restrictions through state transitions

### 2. Greedy + Heap
- Sort by efficiency ratio
- Maintain the best k workers using a max heap

---

## Key Learnings

- Many problems become easier after transforming them into a familiar DP pattern
- Greedy ratio sorting is powerful for cost optimization
- Heap helps maintain the best candidates dynamically

---

## Pattern Recognition

- Adjacent-value restriction → House Robber DP
- Ratio-based optimization → Greedy + Heap

---

## Complexity

### Problem 1
- Time: O(n + max(nums))
- Space: O(max(nums))

### Problem 2
- Time: O(n log n)
- Space: O(n)

---

## Focus Areas

- DP transformations
- Greedy heap optimization