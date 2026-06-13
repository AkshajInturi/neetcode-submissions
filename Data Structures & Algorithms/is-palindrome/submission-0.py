class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal_string = self.build_palindrome_string(s)
        i=0
        j = len(pal_string)-1
        while i < j:
            if pal_string[i] == pal_string[j]:
                i+=1
                j-=1
            else:
                return False
        return True
    
    def build_palindrome_string(self,str):
        result = ""
        for c in str:
            if c.isalnum():
                result+=c.lower()
        return result