class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m ,n = len(grid), len(grid[0])

        memo = {}

        def recurs(i ,j, res):
            if i >=m or j >=n:
                return -1
         
            curr = grid[i][j]

            if i == m-1 and j == n-1:
                return res * curr
            
            if (i,j,res) in memo:
                return memo[(i,j,res)]
            
            right = recurs(i, j+1, res*curr)

            left = recurs(i+1, j, res*curr)

            memo[(i,j,res)] = max(right, left)
            return memo[(i,j,res)]
        
            
        ans = recurs(0, 0, 1)

        if ans > -1:
            return ans % (10**9+7)
        return -1