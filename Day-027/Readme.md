# Day 27 – Knapsack and Subset Sum Dynamic Programming

## Problems Solved

1. Partition Equal Subset Sum
2. Target Sum

## Concepts Learned

- 0/1 Knapsack pattern applied to subset problems
- DP using a set to track reachable sums
- DP using a hash map to count number of ways to reach a target
- Iterating in reverse (or using a copy) to avoid reusing elements

## Key Insight

Both problems reduce to a variant of the 0/1 Knapsack problem.
- **Partition Equal Subset Sum**: check whether any subset sums to `total / 2`.
- **Target Sum**: count all assignments of `+`/`-` to elements that sum to the target — equivalent to counting subsets with a specific sum difference.

## Difficulty Faced

Choosing between bottom-up DP with arrays versus DP with hash maps or sets, and ensuring elements are not reused within a single pass.

## Language

Python
