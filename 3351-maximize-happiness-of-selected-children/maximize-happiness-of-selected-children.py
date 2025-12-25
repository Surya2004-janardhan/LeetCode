class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = [- i for i in happiness]
        heapq.heapify(heap)
        ans = 0
        for i in range(k):
            curr = max(-heapq.heappop(heap) - i, 0 )
            ans += curr

        print(happiness)
        return ans