class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        c=0
        m=neededTime[0]
        for i in range(len(colors)-1):
            
            if colors[i]==colors[i+1]:
                c+=min(neededTime[i+1],m)
                m=max(neededTime[i+1],m)
            else:
                m=neededTime[i+1]
                
        return c