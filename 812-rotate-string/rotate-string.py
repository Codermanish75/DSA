class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # if len(s)!=len(goal):
        #     return False
        # strs=s+s
        # if goal in strs:
        #     return True
        # return False

        strs=s
        n=len(s)
        for i in range(n):
            if strs==goal:
                return True
            strs=strs[-1]+strs[:-1]
        
        return False


        

        