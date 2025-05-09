class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        res=[]

        for i in range(len(nums)):
            if nums[i]>=0:
                p.append(nums[i])
            else:
                n.append(nums[i])
           
        j=0
        k=0
        for i in range(len(nums)):
            if i%2==0 and j<len(p):
                res.append(p[j])
                j+=1
            if i%2!=0 and k<len(n):
                res.append(n[k])
                k+=1
            
        print(res)
        if j<len(p):
            res+=p[j+1:]
        if k<len(n):
            res+=n[k+1:]

        for i in range(len(nums)):
            nums[i]=res[i]
        return nums
                    
            