class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=sorted(list(set(nums)))

        for i in range(len(unique)):
            nums[i]=unique[i]
        
        return len(unique)

        