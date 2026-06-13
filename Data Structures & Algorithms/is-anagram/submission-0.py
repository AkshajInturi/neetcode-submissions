class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        if len(s) != len(t):
            return False
        
        for c in s:
            if c not in freq1:
                freq1[c] = 0
            freq1[c] = int(freq1[c])+1
        for c in t:
            if c not in freq2:
                freq2[c] = 0
            freq2[c] = int(freq2[c])+1

        return freq1 == freq2
        