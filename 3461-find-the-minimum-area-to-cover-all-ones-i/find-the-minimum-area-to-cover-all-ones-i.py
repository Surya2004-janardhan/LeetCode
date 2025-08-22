class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        top, btm, left, right = R,0,C,0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    top = min(top, i)
                    btm = max(btm, i)
                    left = min(left, j)
                    right = max(right, j)
        hei = btm-top+1
        wid = right-left+1
        return hei*wid