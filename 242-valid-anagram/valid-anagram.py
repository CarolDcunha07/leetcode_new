class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}

        if len(s)!=len(t):
            return False

        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1

        for ch in t:
            if ch in freq:
                freq[ch]-=1
            else:
                freq[ch]=1

        print(freq)
        for k,v in freq.items():
            if v!=0:
                return False
        return True
        