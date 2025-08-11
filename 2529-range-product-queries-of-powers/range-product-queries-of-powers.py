class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        i = 0
        mod = 10**9 + 7

        powers = []
        while n:
            if n & 1:
                powers.append(2**i)
            i += 1
            n = n >> 1
        # print(powers)

        prefix = []
        # suffix = []
        prev = 1
        for i in powers:
            prev *= i
            prev = prev % mod
            prefix.append(prev)
        # prev = 1
      
        ans = []

        for i in queries:
            start = i[0]
            end = i[1]
            prev = 1
            for i in range(start, end+1):
                prev *= powers[i]
                prev = prev % mod
            ans.append(prev)
        return ans






        # return []