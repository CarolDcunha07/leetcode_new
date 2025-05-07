class Solution:
    def check(self, nums: List[int]) -> bool:
        i=0
        n=len(nums)-1
        while i < n:
            if nums[i]<=nums[i+1]:
                i+=1
            else:
                break
        if nums[i+1:]+nums[:i+1]==sorted(nums):
            return True
        else:
            return False
        