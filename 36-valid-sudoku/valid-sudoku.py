class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            row = set()
            #col = set()
            for j in i:
                if j == ".":
                    continue
                if j in row:
                    return False
                row.add(j)
        col = set()
        for i in range(9):
            col = set()
            for j in range(9):
                ele = board[j][i]
                if ele == ".":
                    continue 
                elif ele in col:
                    return False
                else:
                    col.add(ele)
                    
        for i in range(9):
            for j in range(9):
                row = (i // 3) * 3
                col = (j // 3) * 3
                sett = set()

                for x in range(3):
                    for y in range(3):
                        element = board[row + x][col + y]
                        if element == ".":
                            continue
                        if element in sett:
                            return False
                        sett.add(element)
                


        return True