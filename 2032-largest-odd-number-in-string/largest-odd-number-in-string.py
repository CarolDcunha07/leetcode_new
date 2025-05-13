class Solution:
    def largestOddNumber(self, num: str) -> str:
        lst=[]
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                lst.append(num[i])
                if lst:
                    lst.append(num[:i])
                    break
        lst=lst[::-1]
        res=''.join(x for x in lst)
        return res
        