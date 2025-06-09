class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q=dividend/divisor 
        
        if q<-2**31:
            return -2**31
        elif q>(2**31)-1:
            return (2**31)-1
        else:
            q=int(q)
            return q
        