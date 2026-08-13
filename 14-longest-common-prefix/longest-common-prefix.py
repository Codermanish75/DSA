class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if n==1:
            return strs[0]
        base=strs[0]
        if len(base)==0:
            return ""
        for i in range(0,len(base)):
            for words in strs[1:]:
                if i==len(words)or words[i]!=base[i]:
                    return base[:i]

        return base
        

        




        