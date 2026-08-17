class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        hash_map={}
        maxi=0
        left=0
        right=0
        while right<n:
            if s[right] in hash_map:
                left=max(left,hash_map[s[right]]+1)

            maxi=max(maxi,right-left+1)
            hash_map[s[right]]=right
            right+=1
        
        return maxi





        