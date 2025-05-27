class Solution:
    def maxDepth(self, s: str) -> int:
        maxc=float('-inf')
        c=0
        lst=[]

        for ch in s:
            if ch=='(':
                c+=1
                lst.append(ch)
            elif ch==')':
                if lst:
                    lst.pop()
                    c-=1
            maxc=max(maxc,c)
        return maxc


        