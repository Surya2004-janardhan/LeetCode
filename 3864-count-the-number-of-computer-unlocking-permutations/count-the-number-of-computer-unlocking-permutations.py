class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        c = complexity
        def fact(n):
            # print(n)
            if n < 1:
                return 1
            return int(n*fact(n-1) % (1e9+7))
        initialComplex = c[0]

        mini = min(c)

        if mini != c[0]:
            return 0
        if c.count(mini) > 1:
            return 0
        return  fact(len(c)-1)
