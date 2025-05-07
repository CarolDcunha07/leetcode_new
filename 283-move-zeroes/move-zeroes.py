class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num=[]
        zero=[]

        for i in range(len(nums)):
            if nums[i]!=0:
                num.append(nums[i])
            else:
                zero.append(nums[i])

        res=num+zero
        for i in range(len(nums)):
            nums[i]=res[i]
        
        