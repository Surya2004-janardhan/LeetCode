class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        totalFreq = Counter(nums)
        prefFreq = {}
        ans = 0

        for i in nums:
            curr = i
            need = i*2
            # if not curr:
            #     continue
            if need in prefFreq:
                if need == 0:
                    ans += prefFreq[need]*(totalFreq[need]-prefFreq[need]-1)

                    
                else:
                    ans += prefFreq[need]*(totalFreq[need]-prefFreq[need])
                # print(ans)
            if curr in prefFreq:
                prefFreq[curr] += 1
            else:
                prefFreq[curr] = 1
        return int(ans%(1e9+7))
