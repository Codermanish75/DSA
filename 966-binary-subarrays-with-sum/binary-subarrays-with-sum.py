class Solution:
    def solve(self,nums,goal):
        if goal<0:
            return 0
        n=len(nums)
        left,right=0,0
        count,total=0,0
        while right<n:
            total+=nums[right]
            while total>goal:
                total-=nums[left]
                left+=1
            
            count+=(right-left+1)
            right+=1
        return count




    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return (self.solve(nums,goal)-self.solve(nums,goal-1))