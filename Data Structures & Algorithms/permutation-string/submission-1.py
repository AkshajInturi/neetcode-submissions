class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        seen = {}

        for c in s1 :
            seen[c] = seen.get(c,0) + 1
        
        window = {}

        left = 0
        for right in range(0,len(s2)):
            c = s2[right]
            window[c] = window.get(c,0) +1

            if right-left+1>len(s1):
                left_char = s2[left]
                window[left_char]-=1
                if window[left_char] == 0:
                    del window[left_char]
                left+=1
            if window == seen :
                return True
        return False