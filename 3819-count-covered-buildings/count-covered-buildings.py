class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        limits = {}

        for i in buildings:
            R = i[0]
            C = i[1]

            if "Rmin"+str(R) in limits:
                limits["Rmin"+str(R)] = min(C, limits["Rmin"+str(R)])
            else:
                limits["Rmin"+str(R)] = C

            if "Rmax"+str(R) in limits:
                limits["Rmax"+str(R)] = max(C, limits["Rmax"+str(R)])
            else:
                limits["Rmax"+str(R)] = C
                
            if "Cmin"+str(C) in limits:
                limits["Cmin"+str(C)] = min(R, limits["Cmin"+str(C)])
            else:
                limits["Cmin"+str(C)] = R
                
            if "Cmax"+str(C) in limits:
                limits["Cmax"+str(C)] =    max(R, limits["Cmax"+str(C)])
            else:
                limits["Cmax"+str(C)] = R
        ans = 0
        for i in buildings:
            R, C = i[0], i[1]

            if limits["Rmin"+str(R)] < C and limits["Rmax"+str(R)] > C and limits["Cmin"+str(C)] < R and limits["Cmax"+str(C)] > R:
               ans += 1

        return ans
                
            


