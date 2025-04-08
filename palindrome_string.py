# It skips commas, spaces, and colons........Compares letters like 'A' and 'a' as equal (case-insensitive)....All characters match → returns True.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start=0
        end=len(s)-1
        while start < end:
            if not s[start].isalnum():
                start+=1
                continue
            if not s[end].isalnum():
                end-=1
                continue
            if s[start].lower()!=s[end].lower():
                return False
            start+=1
            end-=1
        return True
