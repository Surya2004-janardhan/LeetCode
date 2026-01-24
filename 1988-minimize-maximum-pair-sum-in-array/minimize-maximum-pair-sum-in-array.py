class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[0]+nums[-1]
        for i in range(len(nums)//2):
            ans = max(ans , nums[i]+nums[-i-1])
        return ans
