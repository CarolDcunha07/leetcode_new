class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)

        miss=0
        i=0
        print(nums)
        while i<len(nums):
            if nums[i]==miss:
                i+=1
                miss+=1
            else:
                return i
        return i
        