class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        n = len(potions)
        for i in spells:
            min_needed = ceil(success/i)
            # print(min_needed)

            ans = 0

            L = 0
            R = n-1

            while L<=R:

                mid = L + R
                mid //= 2
                # print(mid, potions[mid])

                if potions[mid] >= min_needed:
                    ans = max(ans, n-mid)
                    # print(mid, potions[mid])
                    R = mid-1
                else:
                    L = mid+1
                    

            
            
            res.append(ans)
            
        return res