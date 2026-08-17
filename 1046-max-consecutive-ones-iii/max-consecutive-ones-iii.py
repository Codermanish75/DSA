class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # n=len(nums)
        # maxi=0
        # for i in range(n):
        #     zero=0
        #     for j in range(i,n):
        #         if nums[j]==0:
        #             zero+=1
        #         if zero>k:
        #             break
        #         maxi=max(maxi,j-i+1)
        # return maxi

        n=len(nums)
        left=0
        right=0
        zero=0
        maxi=0
        while right<n:
            if nums[right]==0:
                zero+=1
            while zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi




       
        