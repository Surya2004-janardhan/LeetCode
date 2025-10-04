class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        n=0
        while(i<=j):
            c=j-i
            m=min(height[i],height[j])
            n=max(n,m*c)
            if(min(height[i],height[j])==height[i]):
                i+=1
            else:
                j-=1
        return n      
            
        