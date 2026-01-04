class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        hasher = Counter(nums)
        ans = 0

        def is_4_divisors(num):
            divisors = 1+num
            cnt = 2
            for i in range(2,int(num**0.5)+1):
                if cnt > 4:
                    return False, 0
                if num % i == 0:
                    divisors += i
                    cnt += 1
                    if i != num//i:
                        divisors += num//i
                        cnt += 1
            if cnt == 4:
                return True, divisors

            return False, 0

        for k in hasher:
            valid_num , csum = is_4_divisors(k)

            if valid_num:
                # print(k, csum)
                ans += csum*hasher[k]
        return ans 
