class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            c=nums.count(target)
            idx=nums.index(target)
            return [idx,c+idx-1]
        else:
            return [-1,-1]
        