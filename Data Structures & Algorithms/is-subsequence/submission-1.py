class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = len(s)
        j = len(t)
        mem = [None] * (i)
        for i in range(len(mem)):
            mem[i] = [None] * (j)

        def rec(x, y):
            if y == j:
                return False
            elif x == i:
                return True
            

            elif mem[x][y] != None:
                return mem[x][y]

            elif s[x] == t[y]:
                mem[x][y] = rec(x + 1, y + 1)
                return mem[x][y]

            else:
                mem[x][y] = rec(x, y + 1)
                return mem[x][y]
        return rec(0, 0)

            
        