class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # n=len(nums)
        # count=0
        # for i in range(n):
        #     total=0
        #     for j in range(i,n):
        #         if nums[j]%2==1:
        #             total+=1
        #         if total>k:
        #             break
        #         if total==k:
        #             count+=1
        # return count

        def solve(nums,k):
            n=len(nums)
            left=0
            right=0
            count=0
            total=0
            while right<n:
                if nums[right]%2==1:
                    total+=1
                while total>k:
                    if nums[left]%2==1:
                        total-=1
                    left+=1
                count+=(right-left+1)
                right+=1
            return count

        return solve(nums,k)-solve(nums,k-1)


       
        