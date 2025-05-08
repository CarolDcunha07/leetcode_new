class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        max_c=float('-inf')

        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                c=0
            max_c=max(c,max_c)
        return max_c
        