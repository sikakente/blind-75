from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        hashes = set()
        sequences = set()
        k = 10
        base = 4

        char_mapping = {
            'A': 1,
            'C': 2,
            'G': 3,
            'T': 4
        }

        current_hash = 0
        for i in range(10):
            current_hash = (current_hash * base) + char_mapping[s[i]]
            print(current_hash, i)

        hashes.add(current_hash)

        power = base ** (k-1)

        for i in range(k, n):
            current_hash = current_hash - (char_mapping[s[i-k]] * power)
            current_hash = (current_hash * base) + char_mapping[s[i]]

            if current_hash in hashes:
                sequences.add(s[i-9:i+1])
            else:
                hashes.add(current_hash)

        return list(sequences)
