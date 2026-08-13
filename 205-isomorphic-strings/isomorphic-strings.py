class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s={}
        mapping_t={}
        for i in range(len(s)):
            if s[i] in mapping_s:
                if mapping_s[s[i]]!=t[i]:
                    return False
            else:
                mapping_s[s[i]]=t[i]

            if t[i] in mapping_t:
                if mapping_t[t[i]]!=s[i]:
                    return False
            else:
                mapping_t[t[i]]=s[i]

        return True
            

        