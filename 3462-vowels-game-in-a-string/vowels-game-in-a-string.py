class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # s = list(s)
        # L = 0
        # R = 0
        # print(s)
        # alice = 1
        vow = 0
        for i in s:
            if i in "aeiou":
                vow += 1
        if vow == 0:
            return False
        if vow % 2 == 1:
            return True
        # if total vowels present in the string is EVEN , then alice can simply take EVEN-1 vowels in her turn that leaves
        # bod with a SINGLE vowel and may be some extra charectors 
        # if bod is left with more than 1 char apart from that vowel alice always wins, if left with single char i.e., vowel 
        # then bob lost the game
        # here find the max lenght string with EVEN vowels - 1 vowel
        # need = vow - 1
        # cnt = 0
        # print(need)
        # new_str = []
        # while L <= R and R < len(s):
        #     # print(cnt)
        #     if s[R] in "aeiou":
        #         cnt += 1
        #     if cnt == need:
        #         # print( s[:L] ,s[R:])
        #         new_str = s[:L] + s[R+1:]
        #         break
        #     if cnt > need:
        #         while L < R:
        #             if s[L] in "aeiou":
        #                 cnt -= 1
        #             L += 1
        #     R += 1
        # # new_str = s[:L] + s[R:]
    
        # print(new_str)
        # cnt = 0
        # if len(new_str) > 1 :
        #     return True

        return True

