class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        strs=s+s
        if goal in strs:
            return True
        return False


        

        