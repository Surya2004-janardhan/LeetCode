class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [ [ 0 for i in range(n)] for i in range(m)]
        for i in guards:
            a,b = i[0],i[1]
            grid[a][b] = 'G'
        for i in walls:
            a,b = i[0],i[1]
            grid[a][b] = 'W'

        def bfs(i,j):
            # mark this shit as w so that will be gone in continue

            # mark right
            cnt = 0

            for r in range(j+1, n):
                curr = grid[i][r]
                if curr == 0 or curr == 'B':
                    grid[i][r] = 'B'
                    cnt += 1
                else:
                    break

            # mark left

            for l in range(j-1, -1,-1):
                curr = grid[i][l]
                if curr == 0 or curr == 'B':
                    grid[i][l] = 'B'
                    cnt += 1
                else:
                    break
            # ṃark down

            for d in range(i + 1, m):
                curr = grid[d][j]
                if curr == 0 or curr == 'B':
                    grid[d][j] = 'B'
                    cnt += 1
                else:
                    break
            # mark up

            for u in range(i - 1, -1, -1):
                curr = grid[u][j]
                if curr == 0 or curr == 'B':
                    grid[u][j] = 'B'
                    cnt += 1
                else:
                    break
            # print(cnt)

        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                if curr == 'G':
                    bfs(i, j)
        print(grid)
        return sum( grid[i][j] == 0 for i in range(m) for j in range(n)) 
