\# Day 99 - Phase 3 (Weighted Interval DP + MST Edge Classification)



\## Problems Solved

1\. Maximum Profit in Job Scheduling (Weighted Interval DP)

2\. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree (Kruskal + DSU)



\---



\## Key Concepts



\### 1. Weighted Interval DP

\- Sort jobs by end time

\- Use binary search to find the last compatible job

\- Choose between taking or skipping each job



\### 2. MST Edge Classification

\- Compute the base MST cost

\- Test edges by forcing and excluding them

\- Compare results to classify critical and pseudo-critical edges



\---



\## Key Learnings



\- Interval scheduling becomes easier with binary search + DP

\- Weighted choices require compatibility tracking

\- MST sensitivity checks reveal edge importance clearly



\---



\## Pattern Recognition



\- Non-overlapping profit optimization → weighted interval DP

\- Edge necessity testing → Kruskal + DSU



\---



\## Complexity



\### Problem 1

\- Time: O(n log n)

\- Space: O(n)



\### Problem 2

\- Time: O(E^2 α(V))

\- Space: O(V)



\---



\## Focus Areas



\- Weighted interval DP

\- MST edge classification

