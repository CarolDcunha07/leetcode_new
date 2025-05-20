class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        romans={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

        for a,b in zip(s,s[1:]):
            if romans[a]<romans[b]:
                res-=romans[a]
            else:
                res+=romans[a]
        return res+romans[s[-1]]
        
        