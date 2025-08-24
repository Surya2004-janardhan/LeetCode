class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        t_sum = n*(n+1)
        t_sum //= 2
        ans = 0

        L = 0
        R = 0
        cnt_0 = 0
        for R in range(n):
            if nums[R] == 0:
                cnt_0 += 1
            
            while cnt_0 > 1:
                if nums[L] == 0:
                    cnt_0 -= 1
                L += 1
            
            print(R,L)

            ans = max(ans, R-L)
        return ans
