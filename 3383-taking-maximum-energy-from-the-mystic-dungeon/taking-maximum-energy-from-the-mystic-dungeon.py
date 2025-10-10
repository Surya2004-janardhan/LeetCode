class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        energy = energy[::-1]
        ans = -9876543
        for i in range(k):
            res = 0
            for ind in range(i,len(energy) ,k):
                res += energy[ind]
                ans = max(ans, res)
        return ans