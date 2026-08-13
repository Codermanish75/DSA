class Solution:
    # hbjhb
    def removeOuterParentheses(self, s: str) -> str:
        result=""
        n=len(s)
        count=0
        for ch in s:
            if ch=="(":
                count+=1
                if count>1:
                    result+=ch
            else:
                count-=1
                if count>0:
                    result+=ch
        return result
        