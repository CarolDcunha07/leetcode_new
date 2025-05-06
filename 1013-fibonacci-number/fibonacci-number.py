class Solution:
    def fib(self, n: int) -> int:
        
        return Solution.rec(n)

    @staticmethod
    def rec(n):
        if n==0:
            return 0
        if n==1:
            return 1
        res=Solution.rec(n-1)+Solution.rec(n-2)
        return res
        