# Remove Duplicates from Sorted Array

## Problem Description

Here is a solution to the "Remove Duplicates from Sorted Array" Leetcode problem.

## Solution Overview

The `removeDuplicates` function removes duplicates from a sorted array in-place, returning the count of unique elements.

### Algorithm
- Uses two-pointer technique with index `k` tracking unique elements
- Iterates through the array comparing adjacent elements
- When a new unique element is found, it's placed at position `k`
- Returns the count of unique elements

### Time Complexity
- **O(n)** where n is the length of the array

### Space Complexity
- **O(1)** - operates in-place with constant extra space

## File
- `Remove_Duplicates_Sorted_Array.py` - Contains the solution implementation
