class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        output = True
        for n in range(0, len(s)):
            if s[n] != t[n]:
                output = False
                break

        return output
            
