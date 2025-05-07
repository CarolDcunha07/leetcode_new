class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)

        miss=0

        for i in range(len(nums)+1):
            if i not in nums:
                return i
        