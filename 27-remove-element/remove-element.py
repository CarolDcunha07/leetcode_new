class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lst=[]

        for num in nums:
            if num!=val:
                lst.append(num)
        
        for i in range(len(lst)):
            nums[i]=lst[i]
            
        return len(nums[:len(lst)])
        