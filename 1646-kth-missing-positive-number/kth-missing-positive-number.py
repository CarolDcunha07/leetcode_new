class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        while k>0:
            if i in arr:
                i+=1
            else:
                k-=1
                i+=1
            ans=i
        return ans-1
            