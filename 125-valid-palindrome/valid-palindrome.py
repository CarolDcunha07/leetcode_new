class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum=''
        for ch in s:
            if ch.isalnum():
                alphanum+=ch.lower()
        
        l=0
        h=len(alphanum)-1

        # def pal(l,h,alphanum):
        #     if l>=h:
        #         return
        #     if alphanum[l]!=alphanum[h]:
        #         return False
        #     pal(l+1,h-1)
        if alphanum==alphanum[::-1]:
            return True
        else:
            return False
                
        