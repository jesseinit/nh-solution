
# Find Unique Pairs with Equal Sum

This Python function identifies all unique pairs of integers in a given list that have the same sum. For each sum with multiple pairs, it prints the sum and its corresponding pairs.

## What It Does
- Iterates through all pairs of elements in the input list.
- Groups pairs by their sums.
- Prints only sums that have more than one unique pair.

## Runtime Complexity
1. Pair Generation: O(n^2)  
   - The function generates all possible pairs in the array.
2. Duplicate Check and Insertion: O(m) for each pair, where m is the average number of pairs for a given sum.
3. Processing and Printing: O(k), where k is the number of unique sums.

**Overall Time Complexity:** O(n^2)

## Space Complexity
- Storage for Pairs: O(n^2) in the worst case (if every pair has a unique sum).
- Practical Usage: Much smaller since many sums typically share pairs.

**Overall Space Complexity:** O(n^2)

## How to Run
Execute the function by `python nordhealth.py`.


## Output Example
For the input `[6, 4, 12, 10, 22, 54, 32, 42, 21, 11]`, the output will be:

```
Sum: 16, Pairs: [(6, 10), (4, 12)]
Sum: 54, Pairs: [(12, 42), (22, 32)]
Sum: 33, Pairs: [(12, 21), (22, 11)]
Sum: 32, Pairs: [(10, 22), (21, 11)]
Sum: 64, Pairs: [(10, 54), (22, 42)]
Sum: 43, Pairs: [(22, 21), (32, 11)]
Sum: 53, Pairs: [(32, 21), (42, 11)]
```

For the input `[4, 23, 65, 67, 24, 12, 86]`, the output will be:

```
Sum: 90, Pairs: [(4, 86), (23, 67)]
```