class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_num=nums1+nums2
        sorted_num.sort()
        print(sorted_num)
        if len(sorted_num)%2==0:
            idx=len(sorted_num)//2
            med=(sorted_num[idx-1]+sorted_num[idx])/2
            return med
        else:
            idx=len(sorted_num)//2
            med=sorted_num[idx]
            return med


        