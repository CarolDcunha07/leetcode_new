class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        l=0
        h=len(x)-1

        while l<=h:
            if x[l]==x[h]:
                l+=1
                h-=1
            else:
                return False
        return True
        