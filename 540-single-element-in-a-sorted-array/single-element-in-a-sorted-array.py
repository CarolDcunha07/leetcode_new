class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        freq={}

        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        
        for k,v in freq.items():
            if v==1:
                return k
        