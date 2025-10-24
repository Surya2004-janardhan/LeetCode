class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, 10**9):
            temp = str(i)

            cnt = Counter(temp)
            flag = 0
            # print(cnt)
            for inter in cnt:
                flag = 1
                # print(type(inter), type(cnt[inter]))
                # print(inter, cnt[inter], cnt[str(inter)])
                if cnt[inter] == int(inter):
                    flag = 1
                else:
                    # print("here due to ")
                    flag = 0
                    break
            # print(flag)
            if flag:
                return i
        return i
        
        