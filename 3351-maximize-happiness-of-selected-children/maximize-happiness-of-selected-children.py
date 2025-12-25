class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        ans = happiness[0]
        for i in range(1,k):
            curr = max(happiness[i]-i, 0)
            ans += curr

        print(happiness)
        return ans