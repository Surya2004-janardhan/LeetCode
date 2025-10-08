class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        n = len(potions)
        for i in spells:
            min_needed = ceil(success/i)
            # print(min_needed)

            ps = 0

            L = 0
            R = n-1

            while L<=R:

                mid = L + R
                mid //= 2

                if potions[mid] >= min_needed:
                    ps = n-mid
                    R = mid-1
                else:
                    L = mid+1
                    
            res.append(ps)
            
        return res