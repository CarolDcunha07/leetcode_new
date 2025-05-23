class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 0

        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                return i 
        
        if arr[0]>arr[1]:
            return 0
        if arr[len(arr)-1]>arr[len(arr)-2]:
            return len(arr)-1
        