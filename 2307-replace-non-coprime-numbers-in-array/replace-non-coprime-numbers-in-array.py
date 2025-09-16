class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = [nums[0]]

        def lcm(a, b):
            return abs(a * b) // math.gcd(a, b)

        def check_co_primes(a, b):
            flag = math.gcd(a, b) == 1
            return not flag


        for i in range(1,len(nums)):
            stack.append(nums[i])

            while len(stack) > 1 and math.gcd(stack[-1], stack[-2]) > 1:
                prev = stack[-1]
                prev_prev = stack[-2]
                flag = check_co_primes(prev, prev_prev)
                if flag:
                    lcm_of_2 = lcm(prev, prev_prev)
                    stack.pop()
                    stack.pop()
                    stack.append(lcm_of_2)
        return stack
