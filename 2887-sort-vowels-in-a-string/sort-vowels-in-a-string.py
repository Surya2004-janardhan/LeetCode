class Solution:
    def sortVowels(self, s: str) -> str:
        idk = []
        poi = []
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        for ind,i in enumerate(s):
            if i in vowels:
                idk.append(i)
                poi.append(ind)
        
        idk.sort()
        i = 0
        t = ""
        print(len(idk),len(poi))
        if idk == []:
            return s
        for ind,ele in enumerate(s):
            if i > len(poi)-1 or i > len(idk)-1:
                t += ele

            # print(i,poi[i],idk[i])
            elif ind == poi[i]:
                t += idk[i]
                i += 1
            else:
                t += ele

        return t