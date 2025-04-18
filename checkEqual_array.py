class Solution:
    def checkEqual(self, a, b) -> bool:
        # If lengths differ, they can't be equal
        if len(a) != len(b):
            return False
        
        # Create dictionaries to count frequency manually
        freq_a = {}
        freq_b = {}

        # Count frequency in array a
        for num in a:
            if num in freq_a:
                freq_a[num] += 1
            else:
                freq_a[num] = 1

        # Count frequency in array b
        for num in b:
            if num in freq_b:
                freq_b[num] += 1
            else:
                freq_b[num] = 1

        # Compare frequency dictionaries
        return freq_a == freq_b
