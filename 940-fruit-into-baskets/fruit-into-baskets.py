class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        L = 0
        R = 0
        hasher = {}
        ans = 0
        F = fruits
        while L <= R and R < len(F):
            if F[R] in hasher:
                hasher[F[R]] += 1
            else:
                hasher[F[R]] = 1
            R += 1
            #ans = max(ans, R-L)
            while len(hasher) > 2:
                if hasher[F[L]] > 1:
                    hasher[F[L]] -= 1
                else:
                    del hasher[F[L]]
                L += 1
            ans = max(ans, R-L)
        return ans
            
            
            