class Solution:
    def tribonacci(self, n: int) -> int:
        mem = [None] * (n + 1)

        def h(x):
            if x == 0:
                return 0
            
            elif x == 1 or x == 2:
                return 1

            elif mem[x] != None:
                return mem[x]

            else:
                mem[x] = h(x - 1) + h(x - 2) + h(x - 3)
                return mem[x]

        return h(n)


            