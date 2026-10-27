class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        s = "".join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(s) - 1

        for i in range(len(s)//2):
            if s[i] != s[j]:
                result = False
                break
            j = j - 1

        return result

        