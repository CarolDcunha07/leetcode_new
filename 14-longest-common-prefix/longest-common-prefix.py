class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]

    
        for word in strs[1:]:
            j=0
            while j<len(word) and j<len(prefix) and word[j]==prefix[j]:
                j+=1
            prefix=word[:j]
        
        if prefix:
            return prefix
        else:
            return ''
            
        