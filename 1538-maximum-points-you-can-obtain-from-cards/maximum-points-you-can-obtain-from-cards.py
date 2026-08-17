class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftsum=0
        maxi=0
        n=len(cardPoints)
        if n==k:
            return sum(cardPoints)
        right=n-1
        for i in range(0,k):
            leftsum+=cardPoints[i]
        
        maxi=leftsum
        for i in range(k-1,-1,-1):
            leftsum-=cardPoints[i]
            leftsum+=cardPoints[right]
            right-=1
            maxi=max(maxi,leftsum)

        return maxi
        


            
        