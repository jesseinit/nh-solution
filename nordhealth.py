from collections import defaultdict
from typing import List


def find_unique_pairs_with_equal_sum(arr: List) -> None:
    """
    Finds all unique pairs with the same sum in an array.

    :param arr: List of integers
    :return: None (prints the results directly)
    """
    sum_to_pairs = defaultdict(list)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pair = tuple((arr[i], arr[j]))
            pair_sum = arr[i] + arr[j]

            if pair not in sum_to_pairs[pair_sum]:
                sum_to_pairs[pair_sum].append(pair)

    # Process sums and print pairs
    for pair_sum in sum_to_pairs.keys():
        pairs = sum_to_pairs[pair_sum]
        if len(pairs) > 1:
            print(f"Sum: {pair_sum}, Pairs: {pairs}")


# Example Usage
array1 = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
array2 = [4, 23, 65, 67, 24, 12, 86]

result1 = find_unique_pairs_with_equal_sum(array1)
print("")
result2 = find_unique_pairs_with_equal_sum(array2)
