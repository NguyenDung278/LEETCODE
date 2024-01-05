from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: [int]) -> bool:
        freq_counter = Counter(arr)
        freq_values = freq_counter.values()
        return len(set(freq_values)) == len(freq_values)
