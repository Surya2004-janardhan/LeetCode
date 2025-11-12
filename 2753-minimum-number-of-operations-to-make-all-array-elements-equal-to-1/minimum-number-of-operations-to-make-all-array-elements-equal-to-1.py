class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == sum(nums):
            return 0
        cnt_1 = nums.count(1)
        if cnt_1 > 1:
            return n-cnt_1
        if  1 in nums:
            return n-1 
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        ans = 0
        iter = 50
        while iter:
            ans += 1
            for i in range(n-1):
                temp = gcd(nums[i], nums[i+1])
                if temp == 1:
                    return ans+n-1
                nums[i] = temp
            iter -= 1

        return -1
