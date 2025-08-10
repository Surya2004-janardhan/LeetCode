class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = str(n)
        ans = False
        cnt = Counter(digits)
        for i in range(32):
            power_of_2 = 1 << i

            if not ans:
                ans = Counter(str(power_of_2)) == cnt
            if ans:
                return ans

        return ans
