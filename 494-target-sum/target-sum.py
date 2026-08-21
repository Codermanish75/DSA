class Solution:
    def solve(self,nums,target,n,dp):
        if n==0:
            if target==0:
                return 1
            return 0
        if dp[n][target]!=-1:
            return dp[n][target]
        if nums[n-1]<=target:
            dp[n][target]=(self.solve(nums,target-nums[n-1],n-1,dp)+self.solve(nums,target,n-1,dp))
        else:
            dp[n][target]=(self.solve(nums,target,n-1,dp))

        return dp[n][target]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        total=sum(nums)
        if abs(target)>total:
            return 0
        if (total+target)%2!=0:
            return 0
        subset_target = (total + target) // 2
        dp=[[-1]*(subset_target+1) for _ in range(n+1)]
        return self.solve(nums,subset_target,n,dp)

        