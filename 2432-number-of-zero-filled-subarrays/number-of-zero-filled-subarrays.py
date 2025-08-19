class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for i in nums:
            if i == 0:
                count += 1
                ans += count
            else:
                count = 0
        return ans 