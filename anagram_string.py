class Solution:
    # Function to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        # code here
        if len(s1) != len(s2):
            return False
        
        freq = [0] * 256  # To store frequency of characters
        for char in s1:
            freq[ord(char)] += 1
        for char in s2:
            freq[ord(char)] -= 1
        
        for count in freq:
            if count != 0:
                return False
        return True
