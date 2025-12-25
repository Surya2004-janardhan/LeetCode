class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = [ -i for i in happiness]
        heapq.heapify(heap)
        ans = 0
        for i in range(k):

            curr = -heapq.heappop(heap) - i
            # print(curr)
            if curr > 0:
                ans += curr
            else:
                return ans + max(curr , 0)

        # print(happiness)
        return ans