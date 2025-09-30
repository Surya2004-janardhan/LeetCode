class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        temp = []
        if n == 1:
            return nums[0]
        if n == 2:
            return (nums[0]+nums[1])%10
        steps = n - 1
        while steps:
            # print(nums, temp)
            n = len(nums)
            steps -= 1

            if n == 1:
                return nums[0]

            for i in range(n-1):
                temp.append((nums[i] + nums[i+1])%10)


            nums = temp
            temp = []
        return nums[0]


