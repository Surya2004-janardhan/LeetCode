class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        

        dp =[ [-1 for i in range(n+1)] for i in range(n+1)]
        def rec(c_sum,prev):
            if c_sum == n:
                return 1
            if c_sum > n:
                return 0
            if prev > n:
                return 0
            if dp[c_sum][prev] != -1:
                return dp[c_sum][prev]
            take = rec(c_sum + prev**x,prev + 1)
            not_take= rec(c_sum,prev + 1 )
            dp[c_sum][prev] = (take + not_take) % mod
            return dp[c_sum][prev]
        mod = 10**9+7
        return rec(0,1)
